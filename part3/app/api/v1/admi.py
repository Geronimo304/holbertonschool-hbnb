from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('admin', description='Admin operations')

# MODELOS

admi_model = api.model('Admin', {
    'first_name': fields.String(required=True, description='First name of the admi'),
    'last_name': fields.String(required=True, description='Last name of the admi'),
    'email': fields.String(required=True, description='Email of the admi'),
    'password': fields.String(required=True, description='Password of the admi')
})

# ENDPOINTS 

@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        # Logic to create a new user
        pass

@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = request.json
        email = data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        # Logic to update user details, including email and password
        pass

    @api.route('/<user_id>')
class AdminUserModify(Resource):
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Email already in use')
    @api.response(404, 'User not found')
    @api.response(200, 'User updated successfully')
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt()
        user_id = current_user.get('id')
        if not user_id:
            return {'error': 'Unauthorized action'}, 403

        data = api.payload or {}
        email = data.get('email')

        # Ensure email uniqueness
        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400
        
        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'User not found'}, 404

        return {'message': 'User updated successfully'}, 200

# codigo que ya estsba hecho en user 

@api.route('/')
class AdminUserCreate(Resource):
    @api.expect()
    @api.response(403)
    @jwt_required()
    def post(self):
        try: 
            current_user = get_jwt()
            user_id = current_user.get('id')
            if not current_user.get('is_admin'):
                return {'error': 'Admin privileges required'}, 403

            user_data = api.payload or {}
            email = user_data.get('email')

            # Check if email is already in use
            if facade.get_user_by_email(email):
                return {'error': 'Email already registered'}, 400

            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id,
                'message': 'User created successfully by admin'
            }, 201
        except Exception as e:
            return {'error': str(e)}, 400
