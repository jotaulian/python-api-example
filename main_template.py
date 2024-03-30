from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class ProcessText(Resource):

    def get(self):
        """
        This method responds to the GET request for processing text and returns the processed text.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be processed
            - name: duplication_factor
              in: query
              type: integer
              required: false
              description: Number of times to duplicate the text (default is 1)
            - name: capitalization
              in: query
              type: string
              enum: [UPPER, LOWER, None]
              required: false
              description: Capitalization type for the text (default is None)
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            processed_text:
                                type: string
                                description: The processed text
        """
        text = request.args.get('text')
        duplication_factor = int(request.args.get('duplication_factor', 1))
        capitalization = request.args.get('capitalization')

        processed_text = text * duplication_factor

        if capitalization == 'UPPER':
            processed_text = processed_text.upper()
        elif capitalization == 'LOWER':
            processed_text = processed_text.lower()

        return jsonify({"processed_text": processed_text})

api.add_resource(ProcessText, "/process-text")

if __name__ == "__main__":
    app.run(debug=True)
