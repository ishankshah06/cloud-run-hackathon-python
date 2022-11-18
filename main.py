
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R','T','T','T','T','T','L','R','F','T','T','R','F','T']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    request_input = request.json
    dimsx = request_input['arena']['dims'][0]
    dimsy = request_input['arena']['dims'][1]
    ## getting my position 
    print("new deployment")
    mypos = request_input['_links']['self']['href']
    mylocx = request_input['arena']['state'][mypos]['x']
    mylocy = request_input['arena']['state'][mypos]['y']
    mydirection = request_input['arena']['state'][mypos]['direction']
    washit = request_input['arena']['state'][mypos]['wasHit']

    # if washit == True:
    #     return 'R'
    print(mypos, mylocx, mylocy)
    # if mydirection == 'W':
    #     hitzonex = mylocx + 3
    #     hitzoney = mylocy + 3
    #     if hitzonex > dimsx :
    #         lagdim = hitzonex - dimsx
    #         if lagdim < 3:
    #             lagdimy = dimsy - hitzoney
    #             if lagdimy < 3:
    #                 return 'R'
    #             else:
    #                 return 'L'
    enemyfound = False
    if mydirection == 'N':
        movelocationlag = dimsy - mylocy
        if movelocationlag > 3 :
            for target in request_input['arena']['state']:
                if mypos not in target:
                    enemylocx = target['x']
                    enemylocy = target['y']
                    if enemylocx == mylocx:
                        if enemylocy > mylocy:
                            if enemylocy - mylocy < 3:
                                return 'T'
                                enemyfound = True
    

    if mydirection == 'W':
        movelocationlag = dimsx - mylocx
        if movelocationlag > 3 :
            for target in request_input['arena']['state']:
                if mypos not in target:
                    enemylocx = target['x']
                    enemylocy = target['y']
                    if enemylocy == mylocy:
                        if enemylocx > mylocx:
                            if enemylocy - mylocy < 3:
                                enemyfound = True
                                return 'T'                        
                                
    


            
        
    # TODO add your implementation here to replace the random response
    
    
    return moves[random.randrange(len(moves))]
    # return 'T'

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
