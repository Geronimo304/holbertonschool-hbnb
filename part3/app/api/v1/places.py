from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask import request

api = Namespace('places', description='Place operations')

# Define the models for related entities
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

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    #@jwt_required()
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        data = api.payload
        existing_place = facade.get_place(data['title'])
        if existing_place:
            return {'error': 'Place already exists'}, 400
        
        owner_id = data.get('owner_id')
        if not owner_id: 
            return {'error': 'Owner ID is required'}, 400
        owner = facade.get_user(owner_id)
        if not owner:
            return {'error': 'Owner not found'}, 404
        
        data.pop('owner_id', None) 
        data['owner'] = owner

        n_place = facade.create_place(data)
        return {
            'place_id': n_place.id,
            'title': n_place.title,
            'description': n_place.description,
            'price': n_place.price,
            'latitude': n_place.latitude,
            'longitude': n_place.longitude,
            'owner': {
                'id': owner.id,
                'first_name': owner.first_name,
                'last_name': owner.last_name,
                'email': owner.email
            },
            'amenities': n_place.amenities
        }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        list_place = facade.get_all_places()
        return [{'id': place.id, 'title': place.title, 'price': place.price, 'owner': place.owner.first_name} for place in list_place], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'place not found'}, 404
        return {'title': place.title, 'description': place.description, 'price': place.price, 'latitude': place.latitude, 'longitude': place.longitude, 'owner_id': place.owner.id, 'amenities': place.amenities}, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        place_data = api.payload
        try:
            updated_place = facade.update_place(place_id, place_data)
            return {'message': 'place updated successfully', 'place': {
                'id': updated_place.id,
                'title': updated_place.title,
                'description': updated_place.description,
                'price': updated_place.price,
                'latitude': updated_place.latitude,
                'longitude': updated_place.longitude,
                'amenities': updated_place.amenities
            }}, 200

        except ValueError as e:
            return {'error': str(e)}, 400