from flask import Flask, render_template, request, jsonify

# from chat import get_response

app = Flask(__name__)

def get_response(text):
    output = ''
    # Hi 
    # Hello Sir/Madam, How can I Help you?

    # "What Travel Documents do I need to carry along?"
    # "To book a World Tour, you need passport with 6 months validity subsequent to the scheduled departure date of the tour and with sufficient number of blank pages for visa purposes. You also need to pay a registration amount depending on the tour price. Where as for Indian Tours identification proof and registration amount is required for detailed information on the booking procedure click here."
    # "Will it be possible to extend my stay at a destination?"
    # You can extend your stay provided you intimate us of such extension at the time of your booking. Additional charges will be applicable. No extensions/alterations can be done when the tour is in progress.

    # "What is an e-ticket?"
    # An e-ticket is a paperless electronic document with a unique confirmation number that neatly replaces the hassles of a paper ticket. You may request for a copy to be sent to your e-mail id, in-case of International tours - if & when you require e-tickets for buying Forex, for VISA formalities. For outstation guests who have booked Domestic tours & may arrive at the airport before the scheduled time, we may issue an e-ticket copy if requested for - on a case to case basis, under such circumstances, you are requested to not make any changes in it at the airport as it is a group PNR & any changes may create problem for the entire group!

    # What are the benefits of group bookings?
    # Yes, you are eligible for group discount if you book for a group of more than 8 guests on the same day.

    # What are the modes of travel on tour?
    # The modes of travel depend upon the tour which you book. Generally, we travel by Flight, Coach, Train, Cruise, Speed boat, Jet Foil, Cable Car, etc. as mentioned in the itinerary. For more information refer respective tour itinerary page on the website.
    
    mydict = {
        "Hi":"Hello Sir/Madam, How can I Help you?",
        "What Travel Documents do I need to carry along?":"To book a World Tour, you need passport with 6 months validity along with a Full Vaccination Certificate.For Domestic flights Valid identification card is required along with a Full Vaccination Certificate.",
        "Will it be possible to extend my stay at a destination?":"You can extend your stay provided you intimate us of such extension at the time of your booking. Additional charges will be applicable. No extensions/alterations can be done when the tour is in progress.","What is an e-ticket?":"An e-ticket is a paperless electronic document with a unique confirmation number that neatly replaces the hassles of a paper ticket.",
        "What are the benefits of group bookings?":"Yes, you are eligible for group discount if you book for a group of more than 8 guests on the same day.",
        "What are the modes of travel on tour?":"The modes of travel depend upon the tour which you book. Generally, we travel by Flight, Coach, Train, Cruise, Speed boat, Jet Foil, Cable Car, etc. as mentioned in the itinerary."
    }
    try:
        output = mydict[text]
    except:
        output = 'I do not understand.'

    return output

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True)