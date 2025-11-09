from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('amenities', description='Amenity operations')

# ---- MODELS -----

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

amenity_output_model = api.model('AmenityOutput', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

# ----- ENDPOINTS -----

@api.route('/')
class AmenityList(Resource):
    @jwt_required()
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    def post(self):
        # Create a new amenity
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        amenity_data = api.payload or {}
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return new_amenity, 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.marshal_list_with(amenity_output_model)
    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        # Retrieve a list of all amenities
        amenities = facade.get_all_amenities()
        return amenities, 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.marshal_with(amenity_output_model)
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        # Get amenity details by ID
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        return amenity, 200

    @jwt_required()
    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @api.response(403, 'Admin privileges required')
    def put(self, amenity_id):
        # Update an amenity's information
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        amenity_data = api.payload or {}
        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
        except Exception as e:
            return {'error': str(e)}, 400
        
        if not updated_amenity:
            return {'error': 'Amenity not found'}, 404
        return updated_amenity, 200
