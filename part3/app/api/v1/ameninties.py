from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @jwt_required()
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new amenity"""
        current_user = get_jwt_identity()

        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403
    
        amenity_data = api.payload

        amenity_name = amenity_data.get('name')
        if not amenity_name:
            return {'error':'Amenity name is required'}, 400

        existing_amenity = facade.get_amenity_by_name(amenity_name)

        if existing_amenity:
            return {'error': f'Amenity "{amenity_name}" already registered'}, 400
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {'id': new_amenity.id, 'name': new_amenity.name}, 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        list_amenity = facade.get_all_amenities()
        return [{'id': amenity.id, 'name': amenity.name} for amenity in list_amenity], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 400
        return {'id': amenity.id, 'name': amenity.name}, 201

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, amenity_id):
        """Update an amenity's information"""
        current_user = get_jwt_identity()

        if not current_user.get("is_admin"):
            return {"error": "Admin privileges required"}, 403

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        amenity_data = api.payload
        try:
            updated_amenity = facade.update_amenity(amenity_id, amenity_data)
            return {'message': 'Amenity updated successfully', 'Amenity': {
                'id': updated_amenity.id,
                'name': updated_amenity.name
            }}, 200

        except ValueError as e:
            return {'error': str(e)}, 400