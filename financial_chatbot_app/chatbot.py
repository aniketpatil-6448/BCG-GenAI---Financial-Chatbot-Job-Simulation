import pandas as pd

# Load your financial dataset
df = pd.read_csv("C:/Users/Dell/Desktop/Aniket Resume/Oniline Resume/Data Science/Finance-Chatbot-Project(BCGX)/Finnace-chatbot-project(BCGX).csv")

def simple_chatbot(query):
    query = query.lower()

    if query == "what is the total revenue of microsoft in 2023?":
        value = df[(df['Company'] == 'Microsoft') & (df['Fiscal Year'] == 2023)]['Total Revenue'].values[0]
        return f"The total revenue of Microsoft in 2023 is ${value:,}."

    elif query == "how has net income of apple changed over the last year?":
        apple_2023 = df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2023)]['Net Income'].values[0]
        apple_2022 = df[(df['Company'] == 'Apple') & (df['Fiscal Year'] == 2022)]['Net Income'].values[0]
        diff = apple_2023 - apple_2022
        status = "increased" if diff > 0 else "decreased"
        return f"Apple's net income has {status} by ${abs(diff):,} from 2022 to 2023."

    elif query == "what is the cash flow from operations of tesla in 2022?":
        value = df[(df['Company'] == 'Tesla') & (df['Fiscal Year'] == 2022)]['Cash Flow from Ops'].values[0]
        return f"Tesla's cash flow from operations in 2022 was ${value:,}."

    elif query == "show the revenue growth of all companies in 2023.":
        result = df[df['Fiscal Year'] == 2023][['Company', 'Revenue Growth (%)']]
        return result.to_string(index=False)

    elif query == "what is the net income growth of microsoft in 2022?":
        value = df[(df['Company'] == 'Microsoft') & (df['Fiscal Year'] == 2022)]['Net Income Growth (%)'].values[0]
        return f"The net income growth of Microsoft in 2022 was {value:.2f}%."

    else:
        return "Sorry, I can only respond to predefined financial queries."
