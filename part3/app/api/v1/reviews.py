from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# ---- MODELS ----
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

 # ----- ENDPOINTS -----
@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        # Register a new review
        review_data = api.payload
        user_id = get_jwt_identity() 
        review_data['user_id'] = user_id

        try:
            new_review = facade.create_review(review_data)
            return {
                'id': new_review.id,
                'message': 'Review created successfully'
            }, 201
        except Exception as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        # Retrieve a list of all reviews
        reviews = facade.get_all_reviews()
        return [
            {
                'id': r.id,
                'text': r.text,
                'rating': r.rating,
                'user_id': r.user_id,
                'place_id': r.place_id
            } for r in reviews
        ], 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        # Get review details by ID
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {
            'id': review.id,
            'text': review.text,
            'rating': review.rating,
            'user_id': review.user_id,
            'place_id': review.place_id
        }, 200

    @jwt_required()
    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        # Update a review's information
        current_user = get_jwt_identity()
        review_data = api.payload

        review = facade.get_review(review_id)
        if not updated_review:
            return {'error': 'Review not found'}, 404

        if review.user_id != current_user:
            return {'error': 'Unauthorized action'}, 403

        updated_review = facade.update_review(review_id, review_data)
        return {'message': 'Review updated successfully'}, 200

    @jwt_required()
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        # Delete a review
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        if review.user_id != current_user:
            return {'error': 'Unauthorized action'}, 403

        success = facade.delete_review(review_id)
        if not success:
            return {'error': 'Failed to delete review'}, 400
        return {'message': 'Review deleted successfully'}, 200
       

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        # Get all reviews for a specific place
        reviews = facade.get_reviews_by_place(place_id)
        if reviews is None:
            return {'error': 'Place not found'}, 404
        return [
            {
                'id': r.id,
                'text': r.text,
                'rating': r.rating,
                'user_id': r.user_id,
                'place_id': r.place_id
            } for r in reviews
        ], 200
