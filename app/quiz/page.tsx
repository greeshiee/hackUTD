import React from "react";
import Navbar from "../components/header";
import QuizNavigation from "../components/quiznav"

const questions = {
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

const page = () => {
  return (
    <div className="relative h-screen" id="home">
      <Navbar />
      <div className="flex h-full items-center justify-center px-6 lg:px-8">
      <div className="container mx-auto p-4">
        <h1 className="text-2xl font-bold mb-12 text-left ml-[35%]">Sustainability Quiz</h1>
        <QuizNavigation questions={questions} />
      </div>
      </div>
    </div>
  )
}

export default page