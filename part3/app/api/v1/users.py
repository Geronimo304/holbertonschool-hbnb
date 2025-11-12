from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('users', description='User operations')

# ---- MODELS -----
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

# ---- ENDPOINTS ----

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        # Register a new user
        user_data = api.payload
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
            }, 201

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    @jwt_required()
    def get(self, user_id):
        # Get user details by ID
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            }, 200


@api.route('/<user_id>')
class AdminUserModify(Resource):
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Email already in use')
    @api.response(404, 'User not found')
    @api.response(200, 'User updated successfully')
    @jwt_required()
    def put(self, user_id):
        # Administrador modifica detalles del usuario
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        data = api.payload or {}
        email = data.get('email')

        if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400
        
        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'User not found'}, 404

        return {'message': 'User updated successfully'}, 200



@api.route('/')
class AdminUserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.response(403, 'Admin privileges required')
    @api.response(400,'Email already registered')
    @api.response(201, 'User created successfully by admin')
    @jwt_required()
    def post(self):
        # Administrador crea usuario
        try: 
            current_user = get_jwt()
            if not current_user.get('is_admin'):
                return {'error': 'Admin privileges required'}, 403

            user_data = api.payload or {}
            email = user_data.get('email')

            if email:
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400

            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id,
                'message': 'User created successfully by admin'
            }, 201
        except Exception as e:
            return {'error': str(e)}, 400
