from flask import Flask, jsonify, request
from flask_cors import CORS

import uuid


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/api/*': {'origins': '*'}})

SURVEYS = [
    {
        'id': uuid.uuid4().hex,
        'profile': '',
        'firstname': 'Test',
        'lastname': 'Tester',
        'gender': 'Male',
        'favorite': 'PHP',
        'favorite_why' : 'just like',
        'php' : '10',
        'python' : '10',
        'questions' : 'none'
    },
    {
        'id': uuid.uuid4().hex,
        'profile': '',
        'firstname': 'Test',
        'lastname': 'Tester',
        'gender': 'Male',
        'favorite': 'PHP',
        'favorite_why' : 'just like',
        'php' : '8',
        'python' : '8',
        'questions' : 'none'
    },
    {
        'id': uuid.uuid4().hex,
        'profile': '',
        'firstname': 'Test',
        'lastname': 'Tester',
        'gender': 'Male',
        'favorite': 'PHP',
        'favorite_why' : 'just like',
        'php' : '5',
        'python' : '5',
        'questions' : 'none'
    }
]

@app.route('/api/surveys', methods=['GET', 'POST'])
def all_surveys():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        SURVEYS.append({
            'id': uuid.uuid4().hex,
            'profile': post_data.get('profile'),
            'firstname': post_data.get('firstname'),
            'lastname': post_data.get('lastname'),
            'gender': post_data.get('gender'),
            'favorite': post_data.get('favorite'),
            'favorite_why' : post_data.get('favorite_why'),
            'php' : post_data.get('php'),
            'python' : post_data.get('python'),
            'questions' : post_data.get('questions'),
        })
        response_object['message'] = 'Survey Submitted!'
    else:
        response_object['surveys'] = SURVEYS
    return jsonify(response_object)

@app.route('/api/surveys/<survey_id>', methods=['PUT', 'DELETE'])
def single_survey(survey_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_survey(survey_id)
        SURVEYS.append({
            'id': uuid.uuid4().hex,
            'profile': post_data.get('profile'),
            'firstname': post_data.get('firstname'),
            'lastname': post_data.get('lastname'),
            'gender': post_data.get('gender'),
            'favorite': post_data.get('favorite'),
            'favorite_why' : post_data.get('favorite_why'),
            'php' : post_data.get('php'),
            'python' : post_data.get('python'),
            'questions' : post_data.get('questions'),
        })
        response_object['message'] = 'Survey updated!'
    if request.method == 'DELETE':
        remove_survey(survey_id)
        response_object['message'] = 'Survey removed!'
    return jsonify(response_object)

def remove_survey(survey_id):
    for survey in SURVEYS:
        if survey['id'] == survey_id:
            SURVEYS.remove(survey)
            return True
    return False


if __name__ == '__main__':
    app.run()