from flask import current_app, request
from flask_restx import Namespace, Resource, fields
api = Namespace("amenities", description="Amenity management")


AmenityModel = api.model(
"Amenity",
{
"id": fields.String(readonly=True),
"name": fields.String(required=True),
"description": fields.String,
"created_at": fields.String(readonly=True),
"updated_at": fields.String(readonly=True),
},
)

@api.route("/")
class AmenityList(Resource):
	@api.doc("list_amenities")
	@api.marshal_list_with(AmenityModel)
	def get(self):
		return current_app.facade.list_amenities()

	@api.doc("create_amenity")
	@api.expect(AmenityModel, validate=True)
	@api.marshal_with(AmenityModel, code=201)
	def post(self):
		return current_app.facade.create_amenity(request.json or {}), 201


@api.route("/<string:amenity_id>")
@api.route("/<string:amenity_id>")
@api.param("amenity_id", "Amenity identifier")
class AmenityItem(Resource):
	@api.doc("get_amenity")
	@api.marshal_with(AmenityModel)
	def get(self, amenity_id):
		return current_app.facade.get_amenity(amenity_id)

	@api.doc("update_amenity")
	@api.expect(AmenityModel, validate=False)
	@api.marshal_with(AmenityModel)
	def put(self, amenity_id):
		return current_app.facade.update_amenity(amenity_id, request.json or {})