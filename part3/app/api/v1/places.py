from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('places', description='Place operations')

# ---- MODELS -----

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

place_output_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

place_input_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.Nested(amenity_model), description='List of amenities'),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

# ---- ENDPOINTS -----

@api.route('/')
class PlaceList(Resource):
    @jwt_required()
    @api.expect(place_input_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    def post(self):
        # Register a new place
        try:
            current_user = get_jwt()
            user_id = current_user.get('id')
            if not user_id:
                return {'error': 'Unauthorized action'}, 403
            
            place_data = api.payload or {}
            place_data['owner_id'] = user_id
            new_place = facade.create_place(place_data)
            return {
                'id': new_place.id,
                'message': "Place created successfully"
            }, 201
        except Exception as e:
            return {'error': str(e)}, 400


    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        try:
            places = facade.get_all_places()
            return [p.to_dict() for p in places], 200
        except Exception as e:
            return {'error': str(e)}, 400

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        # Get place details by ID
        try:
            place = facade.get_place(place_id)
            if not place:
                return {'error': 'Place not found'}, 404
            return place.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 400
   
    @jwt_required()
    @api.expect(place_input_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Unauthorized action')
    def put(self, place_id):
        # Update a place's information
        try:
            current_user = get_jwt()
            user_id = current_user.get('id')

            place = facade.get_place(place_id)
            if not place:
                return {'error': 'Place not found'}, 404

            if not is_admin and place.owner_id != user_id:
                return {'error': 'Unauthorized action'}, 403

            place_data = api.payload
            updated_place = facade.update_place(place_id, place_data)
            return updated_place.to_dict(), 200
         
        except Exception as e:
            return {'error': str(e)}, 500
