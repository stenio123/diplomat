#import openai
import pdfplumber
import csv
import re

def read_pdf(file, pages):
    """
    Extract content specified pages in a pdf file and returns as a string.
    If you want to read the entire pdf, use pages == []
    Example 1:
        file = "test.pdf"
        pages = [1,2,3,8]
        read_pdf(file, pages)
    Example 2:
        file = "test.pdf"
        pages = []
        read_pdf(file, pages)
    """
    text = ''
    # Open pdf file and retrieve content of the above pages
    with pdfplumber.open(paperFilePath) as pdf:
        # Check the number of pages in the PDF file
        num_pages = len(pdf.pages)
        print(f"Number of pages in PDF file: {num_pages}")
        if pages == []: pages = list(range(1,num_pages,1))
        
        # Iterate through each page in the index_pages list
        for page_num in index_pages:
            # Check if the page number is valid
            if page_num >= num_pages:
                print(f"Invalid page number: {page_num}")
                continue
            
            # Extract the text from the page
            page_text = pdf.pages[page_num].extract_text()
            if page_text:
                text += " " + page_text
            else:
                print(f"No text found on page {page_num}")
    return text

def remove_dots(input_string):
    """
    Removes the sequence of dots from input string
    """
    # Replace the sequence of two or more dots with !
    return re.sub(r'\.{2,}', '!', input_string)

def remove_sections(input_string):
    """
    Removes any sections that are not under "Recommendations". Assumes starter and end strings.
    """
    
    start = "Recommendations"
    end = "Appendix: "

    start_index = input_string.find(start)
    end_index = input_string.find(end)

    if start_index != -1 and end_index != -1:
        input_string = input_string[start_index:end_index].strip()
        #print(input_string)
    else:
        print("Couldn't find start and/or end markers")
    return input_string

def remove_mid_newlines(input_string):
    """
    Removes any new line chars that are not at the end of a rule name - assumes dots were replaced by '!'
    """
    # Remove any other newlines that are not preceded by an exclamation mark, space, and a number. This is necessary
    # because some rules, like 6.2.6 have new line chars that break the main regex
    # Regex: 
    # # - using negative capture group "(?<! exp) to indicate it should ignore anything matching expression 'exp' 
    # # - [! \d+] representes the sequence exclamation sig, space, any number of digits
    # # - \n is new line "
    return re.sub(r'(?<![! \d+])\n', ' ', input_string)

def extract_rules(input_string):
    """
    After original text is cleaned up, splits up the rules in multiple lines separated by new line char'
    """
    # Regular expression pattern to match the rule number dot, one or multiple times, space and name, ending in exclamation sign, space and a digit
    pattern = r'(\d+\.\d+[.\d+]*)(.*)?\n?(.*)(?:! \d+)'
    # initialize output list with header
    output_list = [['RULE_NUMBER', 'RULE_NAME']]
    # Let's split input string by newline character
    lines = input_string.split('\n')

    # loop through each line and extract rule number and name
    for line in lines:
        match = re.match(pattern, line)
        if match:
            rule_number = match.group(1)
            rule_name = match.group(2)
            # append to output list as a new row
            output_list.append([rule_number, rule_name])
    return output_list

def generate_csv(input_list):
    """
    Generates csv file based on input
    """
    # write output to csv file
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(input_list)

# Pdf file path
paperFilePath = "CIS_benchmarks/CIS_Google_Cloud_Platform_Foundation_Benchmark_v2.0.0.pdf"
#paperFilePath = "CIS_benchmarks/CIS_Amazon_Web_Services_Foundations_Benchmark_v1.5.0.pdf"
# Despite having 300+ pages, let's just focus on the index pages
index_pages = [2,3,4,5, 6]

text = read_pdf(paperFilePath,index_pages)

# If we eventually were to use ChatGPT, to keep track of number of tokens
print("Number of characters before cleanup:", len(text))
text = remove_dots(text)
text = remove_sections(text)
text = remove_mid_newlines(text)
# If we eventually were to use ChatGPT, to keep track of number of tokens
print("Number of characters after cleanup:", len(text))
list = extract_rules(text)
generate_csv(list)


#def GPT_Completion(texts):
## Call the API key under your account (in a secure way)
#  openai.api_key = "API KEY"
#  response = openai.Completion.create(
#    engine="text-davinci-002",
#    prompt =  texts,
#    temperature = 0.6,
#    top_p = 1,
#    max_tokens = 3000,
#    frequency_penalty = 0,
#    presence_penalty = 0
#  )
#  return(response.choices[0].text)

#def create_CSV(input_str):
  # Split the input string into separate lines
#  lines = input_str.splitlines()

  # Create a new CSV file and open it in write mode
#  with open('output.csv', 'w', newline='') as csvfile:
      # Create a csv writer object
#      csvwriter = csv.writer(csvfile, delimiter=',')
      
      # Write the headers to the CSV file
#      csvwriter.writerow(['RULE_NUMBER', 'RULE_NAME'])
      
      # Write the data to the CSV file
#      for line in lines[1:]:
#          fields = line.split(',', maxsplit=1)
#          csvwriter.writerow(fields)

#      print("CSV file created successfully.")

#query = 'With the following text, give me a list of NUMBER and TITLE. In the first example, NUMBER is 1.1 and TITLE is Ensure that Corporate Login Credentials are Used (Manual). In the second, NUMBER is 1.2 and TITLE is Ensure that Multi-Factor Authentication is Enabled for All Non-Service Accounts (Manual)  ' + text
#n=0
#for line in lines:
#    query = "Generate a cvs formatted output following this pattern: \
#        RULE_NUMBER,RULE_NAME \
#        1.1,Ensure that Corporate Login Credentials are Used (Manual) \
#        1.2,Ensure that Multi-Factor Authentication is 'Enabled' for All Non-Service Accounts (Manual) \
#        1.3,Ensure that Security Key Enforcement is Enabled for All Admin Accounts (Manual) \
#        ,only capturing the values that are preceded by a number or a number period another number as RULE_NUMBER, and the text next to it as RULE_NAME, based on this input: " + line
    #result = GPT_Completion(query)

#create_CSV(result)