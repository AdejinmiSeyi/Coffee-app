import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink, db
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
db_drop_and_create_all()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks')
def get_drinks():

    # get drinks using drink.short() data representation
    drinks_list = Drink.query.order_by(Drink.id).all()
    drinks = [drink.short() for drink in drinks_list]

    # check_if_drinks_exists
    if len(drinks_list) == 0:
            abort(404)

    return jsonify({
        "success": True, 
        "drinks": drinks

    }), 200


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])

# 'get:drinks-detail' permission
@requires_auth('get:drinks-detail')
def show_drink(payload):

     # get drinks using drink.long() data representation
    drinks_list = Drink.query.order_by(Drink.id).all()
    drinks = [drink.long() for drink in drinks_list]

    # check_if_drinks_exists
    if len(drinks_list) == 0:
        abort(404)

    #json object body
    return jsonify({
        'success': True,
        'drinks': drinks
    }), 200


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    body = request.get_json()

    try:
        #create new record of drink
        drink = Drink(title=body.get("title", None),
                      recipe=json.dumps(body.get("recipe", None)))

        # check if drink exist
        if not'title' and not 'recipe':
            abort(422)

        #add new drink
        drink.insert()

        # json object response body
        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        })
    except:

        db.session.rollback()
        print(sys.exc_info())
        abort(422)

    finally:
        db.session.close()


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    
    # get drink to be updated by drink_id
    drink = Drink.query.get(drink_id)
    
    # check if drink exist
    if len(drink) == 0:
        abort(404)

    body = request.get_json()

    try:
        # update drink title and recipe
        drink.title = body.get("title", None)
        drink.recipe = json.dumps(body.get("recipe", None))
        drink.update()

        # json object response 
        return jsonify({
            'success': True,
            'drinks': [drink.long()]
        })
    except:
        db.session.rollback()
        print(sys.exc_info())
        abort(422)

    finally:
        db.session.close()


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    # get drink to be deleted by drink id
    drink = Drink.query.get(drink_id)
    
    # check if drink exist
    if len(drink) == 0:
        abort(404)

    try:
        drink.delete()

        return jsonify({
            'success': True,
            'delete': drink.id
        })
    except:
        abort(422)


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
        }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def auth_error(error):
    raise AuthError({
        'code':  error.status_code,
        'description':  error.error
    }, error.status_code)