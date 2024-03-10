import requests

# Gemini API endpoints
SEND_MESSAGE_URL = "https://api.gemini.ai/bot/message"
RECEIVE_MESSAGE_URL = "https://api.gemini.ai/bot/receive"

# Your Gemini API key
API_KEY = "AIzaSyADsWtKTdOdin_ltnZR4-M3MSt073UYa7E"


# Function to send a message to Gemini
def send_message(message):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"message": message}
    response = requests.post(SEND_MESSAGE_URL, headers=headers, json=data)
    return response.json()


# Function to receive messages from Gemini
def receive_message():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(RECEIVE_MESSAGE_URL, headers=headers)
    return response.json()


# Function to perform arithmetic operations
def perform_operation(operation, operands):
    result = None
    if operation == "add":
        result = sum(operands)
    elif operation == "subtract":
        result = operands[0] - sum(operands[1:])
    elif operation == "multiply":
        result = 1
        for operand in operands:
            result *= operand
    elif operation == "divide":
        result = operands[0]
        for operand in operands[1:]:
            result /= operand
    return result


# Main function
def main():
    while True:
        user_input = input("You: ")

        # Send user input to Gemini
        send_response = send_message(user_input)
        print("Message sent to Gemini.")

        # Receive response from Gemini
        receive_response = receive_message()
        if receive_response.get("message"):
            # Check if Gemini's response contains an arithmetic operation
            if receive_response['message'].startswith("calculate"):
                # Extract operation and operands from Gemini's response
                operation, *operands = receive_response['message'].split()[1:]
                operands = [float(operand) for operand in operands]

                # Perform the arithmetic operation
                result = perform_operation(operation, operands)

                # Display the result
                print("Gemini:", result)
            else:
                print("Gemini:", receive_response['message'])
        else:
            print("Gemini did not respond.")


# Execute the main function
if __name__ == "__main__":
    main()
