import flask
from flask import jsonify
from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, GradeEnum
from .schema import AssignmentSchema, AssignmentSubmitSchema
teach = Blueprint('teach', __name__)

@teach.route("/assignments", methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_assignments(p):
    ass = Assignment.get_assignments_by_teacher(p.teacher_id)
    ass_dump = AssignmentSchema().dump(ass, many=True)
    return APIResponse.respond(data=ass_dump)



@teach.route("/assignments/grade", methods=['POST'], strict_slashes=False)
@decorators.auth_principal
def grades_and_stuff(p):
    id = flask.request.json['id']
    if Assignment.check_id_exists(id) == None:
        return jsonify({'error': 'FyleError'}),404
    grade = flask.request.json['grade']
    if not grade in list(GradeEnum):
        return jsonify({'error':'ValidationError'}), 400
    teacher_id = p.teacher_id
    check = Assignment.check_correct_teacher(id, teacher_id)
    if check == None:
        return jsonify({'error': 'FyleError'}),400
    else :
        return jsonify({}),200