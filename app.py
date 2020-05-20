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
        'firstname': 'Freilla Mae',
        'lastname': 'Espinola',
        'gender': 'Female',
        'favorite': ['Python', 'PHP'],
        'favorite_why' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec pharetra ipsum. Quisque egestas est eget felis volutpat pretium sed vel nisl. Pellentesque non pharetra nunc, quis pellentesque dolor. Sed pretium posuere ultrices. Integer dolor ligula, egestas eget mauris a, auctor pellentesque velit. Praesent pellentesque est laoreet, aliquam massa quis, hendrerit risus. Duis scelerisque rhoncus est et euismod. Phasellus vestibulum diam sit amet magna sodales bibendum. Duis nulla nulla, ultricies a mi nec, maximus laoreet purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse id quam eu ipsum tincidunt porta. Donec vitae urna lectus.',
        'php' : '5',
        'python' : '10',
        'questions' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec pharetra ipsum. Quisque egestas est eget felis volutpat pretium sed vel nisl. Pellentesque non pharetra nunc, quis pellentesque dolor.'
    },
    {
        'id': uuid.uuid4().hex,
        'profile': '',
        'firstname': 'Mai',
        'lastname': 'Espinola',
        'gender': 'Female',
        'favorite': ['Python', 'PHP', 'Ruby'],
        'favorite_why' : 'Duis ultrices, est ac aliquet vulputate, lorem lorem consectetur mi, et pulvinar magna leo sit amet nisi. Aenean libero nisi, ornare eget purus non, dignissim lacinia ligula. Praesent vitae erat iaculis, varius quam vitae, blandit risus. In feugiat lacinia leo ac consequat. Aenean eu sem ac odio posuere dignissim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec id euismod nisi. Duis ultricies ligula libero, eu eleifend mi mollis vel. Sed nec condimentum lectus. Fusce felis dolor, placerat et tempus eu, vestibulum cursus arcu',
        'php' : '5',
        'python' : '5',
        'questions' : 'Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc rutrum eget tortor et bibendum. Nullam mollis quis tortor id vestibulum. Duis iaculis luctus nulla, ac interdum ipsum vehicula sit amet. Mauris id arcu odio. Aliquam erat volutpat.'
    },
    {
        'id': uuid.uuid4().hex,
        'profile': '',
        'firstname': 'Mic',
        'lastname': 'Tester',
        'gender': 'Male',
        'favorite': ['PHP'],
        'favorite_why' : 'Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc rutrum eget tortor et bibendum. Nullam mollis quis tortor id vestibulum. Duis iaculis luctus nulla, ac interdum ipsum vehicula sit amet. Mauris id arcu odio. Aliquam erat volutpat.',
        'php' : '2',
        'python' : '2',
        'questions' : 'Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc rutrum eget tortor et bibendum. Nullam mollis quis tortor id vestibulum. Duis iaculis luctus nulla, ac interdum ipsum vehicula sit amet. Mauris id arcu odio. Aliquam erat volutpat.'
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