from openai import OpenAI

client = OpenAI()

def generate_blog(paragraph_topic):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Write a paragraph about the following topic. " + paragraph_topic
    )
    return response.output_text

keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no. ")
    if answer == "Y":
        paragraph_topic = input("What should this paragraph talk about? ")
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
