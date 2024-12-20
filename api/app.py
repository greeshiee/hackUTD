from flask import Flask, request, jsonify, send_from_directory, redirect, url_for

app = Flask(__name__)

questions ={
    "Water Efficiency": [
      {
          "question": "What is the building's current water use in gallons per square foot per year?",
          "type": "number",
          "unit": "gallons/sq ft/year"
      },
      {
          "question": "Are the toilets and sinks designed to save water?",
          "type": "boolean"
      },
      {
          "question": "Is rainwater harvested at the property?",
          "type": "boolean"
      },
      {
          "question": "How much rainwater is collected on average in gallons per month?",
          "type": "number",
          "unit": "gallons/month"
      },
      {
          "question": "Is any of the water on the property recycled?",
          "type": "boolean"
      },
      {
          "question": "How much water is recycled on average as a percentage?",
          "type": "number",
          "unit": "%"
      },
      {
          "question": "Is there an irrigation system on the property?",
          "type": "boolean"
      },
      {
          "question": "How often does irrigation occur?",
          "type": "select",
          "options": ["Daily", "Weekly", "Bi-weekly", "Monthly", "As needed"]
      },
      {
          "question": "How much water is used in gallons per day of irrigation?",
          "type": "number",
          "unit": "gallons/day"
      }
  ],
  "Energy and Atmosphere": [
      {
          "question": "What is the building's current energy use in kBtu per square foot per year?",
          "type": "number",
          "unit": "kBtu/sq ft/year"
          
      },
      {
          "question": "Is there an automated outdoor/hallway lighting system?",
          "type": "boolean"
      },
      {
          "question": "For how many hours does it stay on over the course of 24 hours?",
          "type": "number",
          "unit": "hours"
      },
      {
          "question": "Is it activated by a motion sensor?",
          "type": "boolean"
      },
      {
          "question": "Which of the following renewable energy sources are generated on the property, if any?",
          "type": "multiselect",
          "options": ["Wind", "Solar", "Geothermal"]
      },
      {
          "question": "How much of the property's energy usage is generated by renewable sources as a percentage?",
          "type": "number",
          "unit": "%"
      },
      {
          "question": "What percentage of the building's energy consumption comes from on-site renewable sources or green power purchases?",
          "type": "number",
          "unit": "%"
      }
  ],
  "Materials and Resources": [
      {
          "question": "Has there been a need for repairs due to poor structural design?",
          "type": "boolean"
      },
      {
          "question": "How often is there a need on average?",
          "type": "select",
          "options": ["Never", "Rarely", "Occasionally", "Frequently", "Constantly"]
      },
      {
          "question": "Which of these natural disasters is the location of your property at risk for, if any?",
          "type": "multiselect",
          "options": ["Tornado", "Hurricane", "Earthquake", "Blizzard", "Heat wave", "Landslide/Avalanche", "Flash flooding"]
      },
      {
          "question": "Is the property prone to the \"heat island\" effect?",
          "type": "boolean"
      },
      {
          "question": "Does the property have a recycling, reuse, and/or composting program?",
          "type": "boolean"
      },
      {
          "question": "As a percentage, about how much material generated on the property is recycled, reused, or composted?",
          "type": "number",
          "unit": "%"
      },
      {
          "question": "As a percentage, what proportion of vegetation on your property is a native species?",
          "type": "number",
          "unit": "%"
      }
  ],
  "Indoor Environmental Quality": [
      {
          "question": "On a scale of 1 - 5, how reliant do you believe the property is on artificial indoor lighting?",
          "type": "select",
          "options": ["1", "2", "3", "4", "5"]
      },
      {
          "question": "Are passive heating/cooling techniques used?",
          "type": "boolean"
      },
      {
          "question": "How often are air quality assessments conducted?",
          "type": "select",
          "options": ["Never", "Annually", "Semi-annually", "Quarterly", "Monthly", "Weekly"]
      }
  ]
}

def evaluatewater(answers):
    score = 0

    if answers[0] < 10: #gallon
        score += 1
    if answers[1]: #toilet
        score += 1
    if answers[2]: #harvesting rain water
        score += 1
    if answers[3] > 400: #amount of harvesting
        score += 1
    if answers[4]: #is water recycled
        score += 1
    if answers[5] >= 15: #how much
        score += 1
    if answers[6]: #irrigation
        score += 1
    if answers[7] == "Weekly": ## how often
        score += 1
    if answers[7] == "Bi-weekly": ## how often
        score += 1
    if answers[7] == "Monthly": ## how often
        score += 1
    if answers[7] == "As needed": ## how often
        score += 1
    if answers[8] < 0.5:
        score += 1
#12
def evaluateenergy(answers):
    score = 0

    if answers[0] < 30: # current energy
        score += 1
    if answers[1]: #automated  lighting
        score += 1
    if answers[2] < 14:  #how long it stays on
        score += 1
    if answers[3]: #remote sensor activation
        score += 1
    if answers[4]: #is water recycled
        score += 1
    if answers[5] == "Wind": #if they choose any
        score += 1
    if answers[5] == "Solar": #if they choose any
        score += 1
    if answers[5] == "Geothermal": #if they choose any
        score += 1
    if answers[6] > 40: #how much renewable
        score += 1
    if answers[7] > 20: #how much consumed
        score += 1
#10
def evaluatematerials(answers):
    score = 0

    if answers[0]:
        score += 1
    if answers[1] == "Never":
        score += 1
    if answers[2] == "": ##side note this was supposed to have ai in mind but we didnt have time
        score += 1
    if answers[3]: 
        score += 1
    if answers[4]: 
        score += 1
    if answers[5] > 25: 
        score += 1
    if answers[6] > 90: 
        score += 1
#7
def evaluateindoor(answers):
    score = 0

    if answers[0] == "1":
        score += 1
    if answers[0] == "2":
        score += 1
    if answers[1] :
        score += 1
    if answers[2] != "Never":
        score += 1
#4
@app.route('/submit')
def quiz():
    answers = request.json 
    finalscore = 0
    waterscore, energyscore,matscore,indoorscore = 0
    errors = []
    print("Evaluating Quiz")
    for category, questions in questions.items():
        userAnswers = answers[category]
        for index in enumerate(questions):
            if category == "Water Efficiency":
                score = evaluatewater(answers[category])
                finalscore +=  score
                waterscore += score
            if category == "Energy and Atmosphere":
                score = evaluatewater(answers[category])
                finalscore +=  score
                energyscore += score
            if category == "Materials and Resources":
                score = evaluatewater(answers[category])
                finalscore +=  score
                matscore += score
            if category == "Indoor Environmental Quality":
                score = evaluatewater(answers[category])
                finalscore +=  score
                indoorscore += score
    finalscore = (finalscore*100)/33
    
    return jsonify({
        "score": finalscore,
        "waterscore": waterscore,
        "energyscore": energyscore,
        "matscore": matscore,
        "indoorscore": indoorscore
    })

@app.route('/')
def hello_world():
    return 'Hello, World!'

