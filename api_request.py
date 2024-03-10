import cohere
import json, re
co = cohere.Client('HXsbV5r53c0B94uaC6pcE60ScZhL37Ajr3nB1htX') # This is your trial API key
response = co.generate(
  model='command',
  prompt="""Provide a list of 2 examples in form of Python dictionary of the most common negative thoughts about diversity, women empowerment, self-help, mental issues and underrepresented genders and 4 options for each thought out of which one might be the most correct option. Be sure to mention the correct answer with each thought. Complete the query in under 300 tokens, Only give me the complete python dictionary output do not give any text before the output or after the output.Sample example has been provided: {
    "thoughts": [
        {
            "statement": "Diversity is a joke - it's just another word for less competent women, LGBTQ+, and non-white people taking the places of more competent white men.",
            "options": [
                "The world is a merit-based place",
                "Embrace different perspectives and talents",        
                "Hire people who look like you"
            ],
            "correct": "Embrace different perspectives and talents"  
        },
        {
            "statement": "Women are too sensitive and they just need to get over the microaggressions they experience instead of being so vocal about them.",
            "options": [
                "Keep quiet or it will get worse",
                "Recognize your privilege and speak up",
                "Support and amplify their voices"
            ],
            "correct": "Support and amplify their voices"
        },
        {
            "statement": "Mental health issues are a choice, and people just need to pull themselves up by their bootstraps and stop feeling sorry for themselves.",
            "options": [
                "Mental health is a choice",
                "Seek professional help",
                "Meditate and affirm your way out of depression and anxiety"
            ],
            "correct": "Seek professional help"
        },
        {
            "statement": "Not enough people are talking about men's issues and the unique struggles they face, while everyone is too focused on women's issues.",
            "options": [
                "Focus on women's issues",
                "Ignoring women's issues",
                "Bridge the gap between women's and men's issues"    
            ],
            "correct": "Bridge the gap between women's and men's issues"
        }
    ]
}""",
  max_tokens=500,
  temperature=0.1,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
txt = response.generations[0].text
print(json.dumps(json.loads(txt.strip()), indent=4))

# res = json.loads(txt[4:-3])
# print(json.dumps(res, indent=4))

    


