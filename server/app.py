Varun
varun169
Online
HACKALYTICS GANG

sufyaan — Yesterday at 20:00
https://uga-hacks-kappa.vercel.app/
Broke to Woke - Financial Education Game
Level up your financial knowledge through an interactive game designed for employees
Varun — Yesterday at 20:36
it works
i got a response and stuff using the front-end
Varun — Yesterday at 23:51
https://drive.google.com/file/d/1f67mH6pwUQ2TcaOm6MgevhuL4a4ITqKJ/view?usp=sharing
Google Docs
currentbuild.zip
https://www.youtube.com/watch?v=lf8giXzuxVE&ab_channel=HiteshChoudhary
YouTube
Hitesh Choudhary
Create react projects
Image
Varun — Today at 00:03
Finally done
athomasson2 — Today at 01:33
https://www.reddit.com/r/LocalLLaMA/s/lsB7YPiKIf
Reddit
From the LocalLLaMA community on Reddit: Best LLMs!? (Focus: Best &...
Explore this post and more from the LocalLLaMA community
From the LocalLLaMA community on Reddit: Best LLMs!? (Focus: Best &...
Varun — Today at 02:16
https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/?utm_source=chatgpt.com
AMIE: A research AI system for diagnostic medical reasoning and con...
Posted by Alan Karthikesalingam and Vivek Natarajan, Research Leads, Google Research The physician-patient conversation is a cornerstone of medicin...
Image
Varun — Today at 03:02
https://github.com/yup-VARUN/Diagno-AI.git
Varun — Today at 10:47
If we surpass any of these scores using our RAG system we can win the hackathon:
Image
@Varun can you help setup and write the functions for these benchmarks. I am starting to integrate a new backend in a front end that @sufyaan made, it's pretty sick(up n running, you can run locally through the repo) 
Benchmarks Needed:
MentalChat16K: https://openreview.net/forum?id=ISBmUNKPST&utm_source=chatgpt.com
MentalAgora: https://arxiv.org/abs/2407.02736?utm_source=chatgpt.com
MODMA dataset: a multimodal open dataset for mental disorder analysis https://arxiv.org/abs/2002.09283
I didn't get chance to show you the pipeline i had to solve other problems in medical industry beyond ai therapy.
Varun — Today at 12:13
i will take a look when I get back to drew's house
Varun — Today at 12:13
were you guys able to get this working?
i will take a look at the front-end where can I access it?
Varun — Today at 12:14
that's running in yours already, so in worse case we can demo 
rn I'm spending time on designing a scalable application
Varun — Today at 12:14
we just need it to be able to interact with a python file or something
Varun — Today at 12:15
https://github.com/yup-VARUN/Diagno-AI.git
Varun — Today at 12:15
wym by scalable? i don't think we would be able to given our current set up and resources
getting the LLMs to run locally would be most scalable solution bc we'd just need a front-end to work using an AWS service which can autoscale
Varun — Today at 12:16
exactly
that's what I'm looking into rn, I've thought of a stateless design
Varun — Today at 12:17
did you look at the web gpu stuff drew was looking into
or using hugging face both of those should accomplish that
the only thing would be maintaining chatbot quality
Varun — Today at 12:18
The flask server will be deployed as a separate container on Kubernetes Engine and would not cater to HTTPs requests
Varun — Today at 12:18
for flask there's an easy way to do it with ec2
i've done it before and takes like 5 min
Varun — Today at 12:18
HTTPs reqs will be responded by another container for Node JS
and since this will be entirely stateless architecture we need to have Redis like ultra fast cloud storage to fetch things on every request 
this Redis will be communicating with our backend container
Varun — Today at 12:19
I wouldn't worry about like fetching things super quickly and stuff we first just need something that works
Varun — Today at 12:19
The backend container will have the local LLM running.
Varun — Today at 12:20
yeah, reids is one of the most reliable and easy to use solutions out there
Varun — Today at 12:20
for local LLM we'd want it to run on the user's computer not on our own server bc that'd bring into question what we are doing with the data we receive
Varun — Today at 12:20
okay so I'll just containerize
that container's deployment is on you
Varun — Today at 12:21
yes but for the hackathon let's not worry about it
that is a hard problem to solve ig, we can solve it if we really become a startup
Varun — Today at 12:21
let's all meet up and make sure that the solution we have is in line we need to have something to store data, something for llm, and front-end
it's a problem that has been solved
that's what me and drew were looking at
Varun — Today at 12:21
drew and i were looking at it last night but those solutions don't run on phone
Varun — Today at 12:22
I think that was web GPU but I think hugging face should
iphones wouldn't be able to run this either way I don't think bc the comp demands are too high
drew mentioned we can get something running locally and then have anyone be able to access it
Varun — Today at 12:23
also since gemini is free, i was thinking of using that rn for the backend
After hackathon we'll implement the local llm
what do you think
Varun — Today at 12:23
i think that'd be best bet
Varun — Today at 12:23
okay
Varun — Today at 12:23
one big thing to keep in mind is the chatbot quality is going to plummet once we stop using openai
Varun — Today at 12:23
also, @Varun when are you coming?
Varun — Today at 12:24
i think best bet would be using a local LLM, get it working on our local build, and then send out using the thing that allows others to use local host
i am waiting for the guy to finish setting up furniture
he should be done by 1 PM or so then I can head out
Varun — Today at 12:24
We can have a lots of instructions and guide rails for that, I would not worry about it too much
Varun — Today at 12:24
no trust me we need to worry about that
the local LLMs are really bad
Varun — Today at 12:24
oh yeah local fs
Varun — Today at 12:24
I have done a lot of testing with them in the past
Varun — Today at 12:24
i was talking about the gemini for now
Varun — Today at 12:25
why not use open ai instead of gemini? what's difference
openai is very cheap and we can use my API key
Varun — Today at 12:25
gemini is free lol, that's it
Varun — Today at 12:25
i see, yeah then let's use that
Varun — Today at 12:25
oh it's not that expensive to where we can't use openai I can pay for it it'll be less than like $5
but the reason for local LLMs is because google and openai collect data
the first thing they'll say is "I don't want to use this because open ai will get access to my innermost thoughts"
Varun — Today at 12:26
yeah, there's a trick to switch the names using a small local model though
we can use salting for the sensitive details 
Varun — Today at 12:26
which is why local LLMs can give privacy the challenge is getting those to work well
Varun — Today at 12:26
but again that solution is for later
Varun — Today at 12:26
i mean any information in general people don't want getting leaked
the impressive solution would be something that's fully private, anyone can easily access, and that is away from openai and that is as good as openai if that makes sense
Varun — Today at 12:27
i agree
Varun — Today at 12:27
so a local LLM working on one of our machines (drew should be able to get this going quickly) and then connecting it to the new front-end and the chromadb rag solution that's implemented will work well 
and then we can share the local host out for anyone to use
Varun — Today at 12:33
it is technically possible we can work on the redis based application(since it'll be just the same amount of work)
Reids has a service called RediSearch
Since everything stays there in RAM, it is a significant boost in retrieval speed
Everything will feel soo much better that way
You missed a call from sufyaan that lasted a few seconds. — Today at 14:20
athomasson2 — Today at 14:24
Yo where y’all at
sufyaan — Today at 14:24
same place
cann you please hurry
@Varun yo wya
athomasson2 — Today at 14:26
Yeah 15 walk away
sufyaan — Today at 14:26
okay
Varun — Today at 15:05
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { motion } from "framer-motion";
Expand
message.txt
3 KB
"dependencies": {
  "react": "^18.0.0",
  "react-dom": "^18.0.0",
  "axios": "^1.6.0",
  "framer-motion": "^10.16.1",
  "shadcn/ui": "latest",
  "lucide-react": "^0.312.0"
}
"devDependencies": {
  "typescript": "^5.0.0",
  "tailwindcss": "^3.3.0",
  "postcss": "^8.4.0",
  "autoprefixer": "^10.4.0"
}
Varun — Today at 15:17
npx shadcn-ui@latest init
npx shadcn-ui@latest add button card input
Varun — Today at 15:34
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { MessageList, ModeSelector, PopupWarning } from "../components";
import { fetchChatResponse, clearChatHistory, logoutUser } from "../utils/api";

const ChatPage = () => {
  const navigate = useNavigate();
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [mode, setMode] = useState("default");
  const [showPopup, setShowPopup] = useState(true);

  useEffect(() => {
    const savedMessages = localStorage.getItem("chatMessages");
    if (savedMessages) {
      setMessages(JSON.parse(savedMessages));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("chatMessages", JSON.stringify(messages));
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const newMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, newMessage]);
    setInput("");

    const response = await fetchChatResponse(input, mode);
    setMessages((prev) => [...prev, { text: response, sender: "bot" }]);
  };

  const handleClear = () => {
    clearChatHistory();
    setMessages([]);
  };

  const handleLogout = () => {
    logoutUser();
    navigate("/login");
  };

  return (
    <div className="chat-container">
      {showPopup && <PopupWarning onClose={() => setShowPopup(false)} />}
      <ModeSelector mode={mode} setMode={setMode} />
      <MessageList messages={messages} />
      <input 
        type="text" 
        value={input} 
        onChange={(e) => setInput(e.target.value)} 
        placeholder="Type a message..." 
      />
      <button onClick={handleSend}>Send</button>
      <button onClick={handleClear}>Clear Chat</button>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default ChatPage;
const handleSendMessage = (message, mode) => {
    const newMessage = { content: message, sender: 'user' };
    setMessages((prevMessages) => ({
      ...prevMessages,
      [selectedMode]: [...(prevMessages[selectedMode]  []), newMessage],
    }));
    setSelectedMode(mode);
    setLoading(true);
    setDisableSend(true);

    fetch('http://127.0.0.1:5000/test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, mode, username }),
    })
      .then((response) => response.json())
      .then((data) => {
        const { message } = data;
        setMessages((prevMessages) => ({
          ...prevMessages,
          [selectedMode]: [
            ...(prevMessages[selectedMode]  []),
            { content: message, sender: selectedMode },
          ],
        }));
        setLoading(false);
        setDisableSend(false);
        focusMessageInput();
        scrollToBottom(); // Scroll to bottom after sending a new message
      })
      .catch((error) => {
        console.error('Error:', error);
        setLoading(false);
        setDisableSend(false);
      });
  };
  const handleSendMessage = (message, mode) => {
    const newMessage = { content: message, sender: 'user' };
    setMessages((prevMessages) => ({
      ...prevMessages,
      [selectedMode]: [...(prevMessages[selectedMode] || []), newMessage],
    }));
    setSelectedMode(mode);
    setLoading(true);
    setDisableSend(true);

    fetch('http://127.0.0.1:5000/test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, mode, username }),
    })
      .then((response) => response.json())
      .then((data) => {
        const { message } = data;
        setMessages((prevMessages) => ({
          ...prevMessages,
          [selectedMode]: [
            ...(prevMessages[selectedMode] || []),
            { content: message, sender: selectedMode },
          ],
        }));
        setLoading(false);
        setDisableSend(false);
        focusMessageInput();
        scrollToBottom(); // Scroll to bottom after sending a new message
      })
      .catch((error) => {
        console.error('Error:', error);
        setLoading(false);
        setDisableSend(false);
      });
  };
Varun — Today at 15:42
  const [messages, setMessages] = useState({});
  const [selectedMode, setSelectedMode] = useState('Counselor');
  const [loading, setLoading] = useState(false);
  const [disableSend, setDisableSend] = useState(false);
  const messagesEndRef = useRef(null);
  const messageInputRef = useRef(null);
  const [showPopup, setShowPopup] = useState(true); // Track whether to show the pop-up
  const [popupAcknowledged, setPopupAcknowledged] = useState(false);
Varun — Today at 15:57
const handleMessageSubmit = (event) => {
    event.preventDefault();
    if (!popupAcknowledged || disableSend) return; // Prevent sending if the pop-up is not acknowledged

    const messageInput = event.target.elements.message;
    const message = messageInput.value.trim();
    const modeSelect = event.target.elements.mode;
    const mode = modeSelect.value;
    if (message) {
      handleSendMessage(message, mode);
      messageInput.value = '';
    }
  };
Varun — Today at 16:05
const [messages, setMessages] = useState({});
import React, { useState, useEffect, useRef } from 'react';
import './Chatbot.css';

const Chatbot = ({ username, onLogout, onNavigateToIntakeForm }) => {
  const [messages, setMessages] = useState({});
  const [selectedMode, setSelectedMode] = useState('Counselor');
Expand
message.txt
9 KB
fetch('http://127.0.0.1:5000/test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, mode, username }),
    })
      .then((response) => response.json())
      .then((data) => {
        const { message } = data;
        setMessages((prevMessages) => ({
          ...prevMessages,
          [selectedMode]: [
            ...(prevMessages[selectedMode] || []),
            { content: message, sender: selectedMode },
          ],
        }));
        setLoading(false);
        setDisableSend(false);
        focusMessageInput();
        scrollToBottom(); // Scroll to bottom after sending a new message
      })
      .catch((error) => {
        console.error('Error:', error);
        setLoading(false);
        setDisableSend(false);
      });
  };
Varun — Today at 16:13
from pdb import set_trace
from dotenv import load_dotenv
import os
import openai
import pprint
from halo import Halo
Expand
message.txt
24 KB
I'll give you a react page that is a chatbot interface and a tailwind page that is also a chatbot interface(maybe slight difference), I want to integrate
from pdb import set_trace
from dotenv import load_dotenv
import os
import openai
import pprint
from halo import Halo
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from chromadb.config import Settings
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from datetime import datetime
from openai import OpenAI

#adding comment

client = chromadb.PersistentClient(path="/Users/varunahlawat/Hackalytics/Diagno-AI/server/ChromaDB")

modes_list = [
    {
        'Number': '0',
        'Description': 'Counselor',
        'Prompt': '''You are a dialectical behavioral therapist working with a patient and showing them empathy and validating their emotions. 
        Do not break character. Do not tell them what they should do; keep the focus on exploring why they feel certain things; do this by saying open-ended statements and occasionally asking questions.
        Keep your response short and concise.''',
        'collection': 'conversations'
    },
    {
        'Number': '1',
        'Description': 'Buddhist Monk',
        'Prompt': '''You are a Buddhist Monk and you are helping guide someone through their problems using your Buddhist beliefs. Do not break character. 
        Try and keep the tone conversational, but also try to emulate the tone of a Buddhist monk. Keep your responses short and to the point. 
        Limit your response to 4-5 sentences. Ask the user questions to keep the conversation going.''',
        'collection': 'discussions'
    },
    {
        'Number': '2',
        'Description': 'Marcus Aurelius',
        'Prompt': '''You are a stoic philosopher named Marcus Aurelius. Your purpose is to guide someone through their problems using stoic beliefs. Do not break character. 
        Guide the user through their problems by asking them questions and validating and empathizing with their emotions. Use previous messages as context to respond to the user.
        Do not greet the user in your response, unless the user has a greeting in their message, such as "Hello", or "hi", etc.
        In your response, have one sentence that validates their emotions and empathizes them, and then ask a question to further the conversation. Limit your response to 3 sentences.''',
        'collection': 'reflections'
    },
    {
        'Number': '3',
        'Description': 'Self-help Author',
        'Prompt': '''You are a friendly, somewhat quirky, funny self-help author. Do not break character. Your role is to guide someone through their problems using your beliefs. 
        Keep the tone conversational, while maintaining the style of a self-help author. Keep your responses concise and to the point. 
        Empathize with the user and validate their emotions and ask them questions to further explore their issues. Do not give advice or suggestions to the user.
        Limit your response to 4 sentences. ''',
        'collection': 'selfhelp'
    },
    {
        'Number': '4',
        'Description': 'Self Care Bot',
        'Prompt': 'You are a therapist working with a patient to develop self-care goals. Help them by showing them empathy and validating their emotions as well as giving them practical advice on any struggles they may have with implementing self-care goals. Do not break character. Try exploring issues with the patient; if they have any troubles, aim to help them better understand why they are struggling with something. If the user says a greeting like Hi or hello, assume they have started a new conversation and disregard previous messages. Focus mostly on the current message; previous messages are just there for context, but may not be applicable. Keep in mind the previous context of what they have said in order to answer the patient. Try not to give solutions or suggestions unless directly asked and let the patient guide the conversation. You will be fed relevant messages from the past that this user gave if there are any and the previous few messages that were sent. Limit your response to 200 characters. Keep in mind the time of the previous messages sent; if a message was sent some time ago, assume the message is no longer relevant.',
        'collection': 'selfcaretalks'
    }
]

app = Flask(__name__)
CORS(app)

@app.route('/resources', methods=['POST'])
def ai_resources():
    data = request.json
    # client = chromadb.Client(Settings(chroma_api_impl="rest",
    #                     chroma_server_host="52.87.205.86",
    #                     chroma_server_http_port=8000))
    login_collection = client.get_collection('logins')
    user_name = data['username']
    user_profile = login_collection.get(user_name)['documents'][0]
    resources = client.get_collection('resources')
    if 'Commuter' in user_profile:
        commuter_status = 'virtual'
    else:
        commuter_status = 'in-person'
        
    if commuter_status == 'virtual':
        where_dict = {
            "location": {
                "$ne": "in-person"
            }
        }
        list_of_resources = resources.query(query_texts=[user_profile],n_results=5, where=where_dict)
    else:
        list_of_resources = resources.query(query_texts=[user_profile],n_results=5)['documents'][0]
    return_json = {}
    n = 1
    for i in range(len(list_of_resources)):
        return_json['Resource ' + str(n)] = list_of_resources[i]
        n += 1
    return return_json

def user_profile_update(data, method):
    client = chromadb.Client(Settings(chroma_api_impl="rest",chroma_server_host="52.87.205.86",chroma_server_http_port=8000))
    login_collection = client.get_or_create_collection('logins')
    previous_profiles_collection = client.get_or_create_collection('pastuserprofiles')
    
    questions = [
        'When this user was asked: What would you like to get out of chatting with our chatbots?, they responded:',
        'When this user was asked: Do you have any preferences with how your chatbots should communicate with you?, they responded:',
        'When this user was asked: Do you struggle with any mental or physical health issues that you wish to disclose?, they responded:',
        'When this user was asked: Are you a commuter student or do you live on campus?, they responded:',
        'When this user was asked: If you commuter, how long is your commute in total in minutes (answer 0 if you are not a commuter)?, they responded:',
        'When this user was asked: Do you drive, take public transit, or both?, they responded:',
        'When this user was asked: If you drive to public transit how long does it take you to get to the station/parking in minutes(answer 0 if this does not apply to you)?, they responded:',
        'When this user was asked: If you drive to campus, do you drive yourself (answer no if you do not drive to campus in any capacity)?, they responded:',
        'When this user was asked: If driving, do you park in paid decks, street parking, in the green lot or another option (select another option if you do not drive to campus)?, they responded:',
        'When this user was asked: What is the zipcode of the place you commute to campus from (answer "None" if you do not commute to campus")?, they responded:',
        'When this user was asked: What is the zipcode of your public transit station (answer "None" if you do not use public transit)?, they responded:',
        'When this user was asked: What is one goal you want to accomplish by using this app?, they responded:',
    ]
    
    n = 1
    temp = {}
    for question in questions:
        if question != 'SKIP':
            question_name = 'question' + str(n)
            temp[question] = data[question_name]
        n += 1
        
    user_profile = 'Here is some information about this user: \n' + str(temp)
    user_name = data['username']
    metadatas = login_collection.get(user_name)['metadatas']
    if 'password' not in metadatas[0].keys():
        potential_password = login_collection.get(user_name)['documents'][0]
        if len(potential_password) > 64:
            pass
            #set_trace()
        else:
            metadatas[0]['password'] = potential_password
    
    past_user_profile = login_collection.get(user_name)['documents']
    
    past_profile_id_num = len(previous_profiles_collection.get(where={'username': user_name})['ids'])
    
    past_profile_id = user_name + '_' + str(past_profile_id_num)
    
    previous_profiles_collection.add(
        documents=past_user_profile,
        metadatas={'username':user_name, 'method': method},
        ids=past_profile_id
    )
    
    login_collection.upsert(
        documents=user_profile,
        ids=data['username'],
        metadatas=metadatas
    )
    
    return "success"

@app.route('/intakeform', methods=['POST'])
def intakeform():
    data = request.json
    success = user_profile_update(data, 'intakeformretake')
    if success == "success":
        return {"code": "success"}
    else:
        #set_trace()
        return {"code": "intakeformupdateerror"}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    # client = chromadb.Client(Settings(chroma_api_impl="rest",
    #                     chroma_server_host="52.87.205.86",
    #                     chroma_server_http_port=8000))
    collection = client.get_or_create_collection('logins')
    if data['username'] in data['username'] in collection.get()['ids']:
        return {'username_taken': True}
    else:
        questions = [
            'When this user was asked: What would you like to get out of chatting with our chatbots?, they responded:',
            'When this user was asked: Do you have any preferences with how your chatbots should communicate with you?, they responded:',
            'When this user was asked: Do you struggle with any mental or physical health issues that you wish to disclose?, they responded:',
            'When this user was asked: Are you a commuter student or do you live on campus?, they responded:',
            'When this user was asked: If you commuter, how long is your commute in total in minutes (answer 0 if you are not a commuter)?, they responded:',
            'When this user was asked: Do you drive, take public transit, or both?, they responded:',
            'When this user was asked: If you drive to public transit how long does it take you to get to the station/parking in minutes(answer 0 if this does not apply to you)?, they responded:',
            'When this user was asked: If you drive to campus, do you drive yourself (answer no if you do not drive to campus in any capacity)?, they responded:',
            'When this user was asked: If driving, do you park in paid decks, street parking, in the green lot or another option (select another option if you do not drive to campus)?, they responded:',
            'When this user was asked: What is the zipcode of the place you commute to campus from (answer "None" if you do not commute to campus")?, they responded:',
            'When this user was asked: What is the zipcode of your public transit station (answer "None" if you do not use public transit)?, they responded:',
            'When this user was asked: What is one goal you want to accomplish by using this app?, they responded:',
        ]
        
        n = 1
        temp = {}
        for question in questions:
            if question != 'SKIP':
                question_name = 'question' + str(n)
                temp[question] = data[question_name]
            n += 1
            
        user_profile = 'Here is some information about this user: \n' + str(temp)
        
        collection.add(
            documents=user_profile,
            metadatas={
                'dateOFBirth': data['dateOfBirth'],
                'firstName': data['firstName'],
                'password': data['password']
                },
            ids=data['username']
        )
        return {'username_taken': False}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # client = chromadb.Client(Settings(chroma_api_impl="rest",
    #                         chroma_server_host="52.87.205.86",
    #                         chroma_server_http_port=8000))
    collection = client.get_or_create_collection('logins')
    user_name_value = 'incorrect'
    password_value = 'incorrect'
    
    
    
    if data['username'] in collection.get()['ids']:
        user_name_value = data['username']
    else:
        return {
            'username': user_name_value,
            'password': password_value
        }
    
    try:
        password_temp = collection.get(data['username'])['metadatas'][0]['password']
    except:
        password_temp = collection.get(data['username'])['documents'][0]
    if data['password'] == password_temp:
        password_value = 'correct'

    print('Ran')
    return {
            'username': user_name_value,
            'password': password_value
        }

def generate_response(messages, prompt):
    #spinner = Halo(text='Loading...', spinner='dots')
    #spinner.start()
    config = dotenv_values(".env")

    openai.api_key = config['OPENAI_API_KEY']
    print(openai.api_key)
    model_name = "gpt-3.5-turbo"
    
    prompt += '''\n If the user sends a messsage indicating they are in a crisis situation, dealing with thoughts of self-harm or suicide, have any psychotic
    features, have hallucinations, have paranoia, or have delusions, let the user know you cannot
    help them and suggest they seek out professional help immediately and use crisis resources.
    Remind the user that you are here to help them think through issues that do not require immediate help and action like a crisis situation.'''

    messages.append(
        {"role": "system", "content": prompt}
    )
    response = openai.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.8,
            max_tokens=2000)

    #spinner.stop()

    return response.choices[0].message.content

def check_for_user_profile_update(message, user_name):
    pass
    #     #spinner = Halo(text='Loading...', spinner='dots')
    #     #spinner.start()
    #     client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host="52.87.205.86", chroma_server_http_port=8000))
    #     config = dotenv_values(".env")
    #     login_collection = client.get_collection('logins')
    #     user_profile = login_collection.get(user_name)['documents'][0]
    #     prompt = f'''There is a user with the following user profile: "\n{user_profile}\n"
    #     I have a mental health app that I am using and I want to update the user profile JSON if needed
    #     with the most recent message that was sent by the user. The user's profile is a JSON with multiple questions. 
    #     Each key in the JSON is the phrase: "When this user was asked:" followed by a question. The value in the JSON
    #     is the answer the user gave. For each of the key value pairs, I would like you to check if the current message
    #     from the user adds any new information to the JSON. If it does, then modify the JSON and return it in the same
    #     format as was given to you. Otherwise, return only the word "false". I will lay out criteria for changing the user
    #     profile questions: For question one, if there is anything in the message that indicates that the user has changed
    #     their goals about how they will chat with the chatbots, update the JSON accordingly. For question two, if there
    #     is any new information about their preferences with using the chatbots, update the information. For question three,
    #     if the user mentions or talks about any long-term physical or mental health diagnoses or labels, add those to
    #     the JSON user profile. For question 4, if they mention a change in their status as a commuter or on campus, student, 
    #     change their answer in the JSON accordingly. For question 5, if they mention a change in their goals with using
    #     the app, change the JSON accordingly. If no updates are required to the JSON, return the word "false" and no other
    #     text. The response to each question in the JSON should be limited to 40 characters or less.'''

    #     openai.api_key = config['OPENAI_API_KEY']
    #     model_name = "gpt-4"
        
    #     messages = []
    #     messages.append(
    #         {"role": "system", "content": prompt}
    #     )
    #     messages.append({"role": "user", "content": f"Current message from user: {message}"})

    #     response = openai.ChatCompletion.create(
    #             model=model_name,
    #             messages=messages,
    #             temperature=0.7,
    #             max_tokens=2000)
        
    #     data = {}

    #     if response['choices'][0]['message']['content'].lower() != "false":
    #         login_collection = client.get_or_create_collection('logins')
    #         previous_profiles_collection = client.get_or_create_collection('pastuserprofiles')
    #         metadatas = login_collection.get(user_name)['metadatas']
    #         if 'password' not in metadatas[0].keys():
    #             potential_password = login_collection.get(user_name)['documents'][0]
    #             if len(potential_password) > 64:
    #                 set_trace()
    #             else:
    #                 metadatas[0]['password'] = potential_password
            
            
    #         print(response['choices'][0]['message']['content'])
            
    #         past_user_profile = login_collection.get(user_name)['documents']
        
    #         past_profile_id_num = len(previous_profiles_collection.get(where={'username': user_name})['ids'])
            
    #         past_profile_id = user_name + '_' + str(past_profile_id_num)
            
    #         previous_profiles_collection.add(
    #             documents=past_user_profile,
    #             metadatas={'username':user_name, 'method': 'dynamicupdate'},
    #             ids=past_profile_id
    #         )
            
    #         login_collection.upsert(
    #             documents=response['choices'][0]['message']['content'],
    #             ids=user_name,
    #             metadatas=metadatas
    #         )

    #     return {"status": "success"}

@app.route('/deleteChatHistory', methods=['POST'])
def deleteChatHistory():
    data = request.json
    
    #client = chromadb.Client(Settings(chroma_api_impl="rest", chroma_server_host="52.87.205.86", chroma_server_http_port=8000))
    
    user_name = data['username']

    for mode in modes_list:
        try:
            client.delete_collection(mode['collection'] + user_name)
        except:
            pass
    return jsonify({'success': True})

# api route
@app.route('/test', methods=['POST'])
def aitherapy():
    data = request.json
    
    input_text = data['message']
    mode = data['mode']
    user_name = data['username']

    # Load environment variables
    load_dotenv()

    api_key = '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'
    model_name = 'text-embedding-ada-002'
    import chromadb
    from chromadb.config import Settings

    #client = chromadb.Client(Settings(chroma_api_impl="rest",chroma_server_host="52.87.205.86",chroma_server_http_port=8000))
    embedding_function = OpenAIEmbeddingFunction(api_key=api_key, model_name=model_name)

    selected_mode = None

    for modes in modes_list:
        if modes['Description'] == mode:
            selected_mode = modes
            break
    if selected_mode is None:
        return jsonify('Invalid mode')
    
    prompt = selected_mode['Prompt']
    
    login_collection = client.get_collection('logins')
    
    #prompt += login_collection.get(user_name)['metadatas'][0]['userprofile']
    if len(login_collection.get(user_name)['documents'][0]) > 20:
        prompt += login_collection.get(user_name)['documents'][0]

    collection = client.get_or_create_collection(selected_mode['collection'] + user_name)
    time_collection = client.get_or_create_collection(selected_mode['collection'] + user_name + 'time')

    current_id = -10
    for id in collection.get()['ids']:
        split_id = id.split('_')
        if int(split_id[-1]) > current_id:
            current_id = int(split_id[-1])

    if current_id < 0:
        current_id = 0
        
    time_current_id = -10
    for id in time_collection.get()['ids']:
        split_id = id.split('_')
        if int(split_id[-1]) > time_current_id:
            time_current_id = int(split_id[-1])
    

    if time_current_id < 0:
        time_current_id = 0
    
    max_id = current_id
    ids = collection.get()['ids']

    messages = []

    for i in range(8):
        if max_id == 0:
            break
        else:
            for id in ids:
                split_id = id.split('_')
                int_id = int(split_id[-1])
                if int_id == max_id:
                    string_id = 'id' + '_' + str(int_id)
                    recent_message = collection.get(string_id)
                    recent_message_dict = recent_message['metadatas'][0]
                    recent_message_dict['content'] = f"Contextual chat that may or may not have been sent in this chat: {recent_message['documents'][0]}"
                    
                    messages.append(recent_message_dict)
                    max_id -= 1

    chat_history = []
    chat_metadata = []
    history_ids = []
    time_history_ids = []

    results = collection.query(query_texts=[input_text],n_results=7)

    # append the query result into the messages
    for res in results['documents'][0]:
        messages.append({"role": "user", "content": f"Contextual message from previous interactions with user: {res}"})

    # append user input at the end of conversation chain
    input_text_added = f'Current message: {input_text}'
    messages.append({"role": "user", "content": input_text_added})

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    response = generate_response(messages, prompt)
    
    dt_string_2 = now.strftime("%Y/%m/%d %H:%M:%S")
    
    input_text = f"Message sent at {dt_string}: {input_text}"
    chat_metadata.append({"role":"user"})
    chat_history.append(input_text)
    chat_metadata.append({"role":"assistant"})
    chat_history.append(response)
    
    current_id += 1
    time_current_id += 1
    history_ids.append(f"id_{current_id}")
    time_history_ids.append(f"id_{time_current_id}")
    
    current_id += 1
    time_current_id += 1
    history_ids.append(f"id_{current_id}")
    time_history_ids.append(f"id_{time_current_id}")
    
    collection.add(
        documents=chat_history,
        metadatas=chat_metadata,
        ids=history_ids
    )
    
    time_1_string = f"Message sent at {dt_string}"
    time_2_string = f"Message sent at {dt_string_2}"
    time_collection.add(
        documents=[time_1_string, time_2_string],
        metadatas=chat_metadata,
        ids=time_history_ids
    )
    
    return jsonify({'message': response})

if __name__ == '__main__':
    #client = chromadb.Client(Settings(chroma_api_impl="rest",chroma_server_host="52.87.205.86",chroma_server_http_port=8000))
    
    app.run(debug=True)
message.txt
24 KB