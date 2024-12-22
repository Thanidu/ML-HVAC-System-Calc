import json
import pickle
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings


# Load the model
MODEL_PATH = os.path.join(settings.BASE_DIR, 'HVAC', 'model', 'hvac.pickle')

with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

def chiller_input(request):
    if request.method == "POST":
        try:
            # Parse the input parameters from the request
            generator_duty = float(request.POST.get("generatorDuty"))
            pump_pressure = float(request.POST.get("pumpPressure"))
            mass_flow_rate = float(request.POST.get("massFlowRate"))
            chiller_input = float(request.POST.get("chillerInTemp"))

            # Prepare the input for the ML model
            input_data = [[generator_duty, pump_pressure, mass_flow_rate]]

            # Get predictions from the ML model
            prediction = model.predict(input_data)
            

            # Format the results (Assume the model returns an array of values)
            results = {
                "output_temp": round(chiller_input-(12 - prediction[0][0]), 3),  # Chiller Output Temp
                "evaporator_duty": round(prediction[0][1], 3),  # Duty of Evaporator
                "generator_output": round(prediction[0][2], 3),  # Generator Output Temp
                "cop": round(prediction[0][1] / generator_duty, 3), #cop calculation            
            }

            # Return results as a JSON response
            return JsonResponse(results)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # Render the form for GET requests
    return render(request, "index.html")