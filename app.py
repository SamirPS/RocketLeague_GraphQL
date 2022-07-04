from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listTeams_resolver,getTeam_ByName_resolver,listRegions_resolver,listPlayers_resolver,getPlayer_ByName_resolver,getTeam_ByRegion_resolver

query = ObjectType("Query")

query.set_field("listAllTeams", listTeams_resolver)
query.set_field("getTeam_ByName", getTeam_ByName_resolver)
query.set_field("getTeam_ByRegion", getTeam_ByRegion_resolver)


query.set_field("listAllRegions", listRegions_resolver)

query.set_field("listAllPlayers", listPlayers_resolver)
query.set_field("getPlayer_ByName", getPlayer_ByName_resolver)



type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route("/", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code