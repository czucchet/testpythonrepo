

#-------- 1 install required packages -----#
# py -m pip install openai
# py -m pip install Levenshtein
import openai
############################################


# build an idea bot that can generate ideas
# https://beta.openai.com/docs/engines/idea

#-------- 2 set API key -----#
import os
import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

#-------- 3 run an example chatgpt api to create a series of product recommendations -----#

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Product description: A home milkshake maker\nSeed words: fast, healthy, compact.\nProduct names: HomeShaker, Fit Shaker, QuickShake, Shake Maker\n\nProduct description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit.",
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response)

#-------- 4 change working directory and save the result to this directory -----#
# change working directory

os.chdir(r"C:\Users\czucche\Desktop\Use Case Development\ChatGPT\1) Outputs")

with open('response.txt', 'w') as outfile:
    json.dump(response, outfile)

cwd = os.getcwd()
print(cwd)

# take the response object and parse it to get the product names

#-------- 5 parse the response object to get the product names -----#

# get the product names
product_names = response['choices'][0]['text']
#write the product_names to a csv
with open('product_names.csv', 'w') as f:
    f.write(product_names)
















