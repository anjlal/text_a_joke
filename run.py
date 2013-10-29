from flask import Flask, render_template, request, redirect, session, url_for, flash
import twilio.twiml
import model
import random

app = Flask(__name__)
app.secret_key = '\xfb\xb1\xa4\x1e\x9a\x83\x1em\x82\x07El3\x9bI\xfa\xc5\xe5\xdd\xc4\x9a\xf9\xc6g'

# Try adding your own number to this list!
# callers = {
#     "+14085070117": "Poo",
#     "+14088074454": "Angie",
# }
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
   """Respond to incoming calls with a simple text message."""
   counter = session.get('counter', 0)

   # increment the counter
   counter += 1
   
   # Save the new counter value in the session
   session['counter'] = counter
   # 
   # from_number = request.values.get('From')
   # if from_number in callers:
   # 		name = callers[from_number]
   # else:
   #     name = "Joker"
   if session.get('counter') == 1:
       # model.init_db()
       question, answer = model.get_joke_by_id(1)
   else:
       count = model.count_jokes()
       rand_num = random.randint(1, int(count) + 1)
       question, answer = model.get_joke_by_id(rand_num)
   message = "".join(["Why so serious?: ", question, " ", answer])
   
# , " ", 
   #     str(counter), " times."])
   resp = twilio.twiml.Response()
   resp.sms(message)
   
   return str(resp)

if __name__ == "__main__":
	app.run(debug=True)