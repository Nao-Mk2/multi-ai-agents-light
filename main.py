import json
import sys
import agent.master

def main():
  """Main function to run the agent with a task from command line arguments."""
  try:
    request = json.loads(sys.argv[1])

    master_agent = agent.master.wake_up()
    
    # Execute the task and get the response
    response = master_agent.invoke({"input": request['task']})
    
    # Extract the output from the response
    if isinstance(response, dict):
        if 'output' in response:
            result = {"response": response['output']}
        elif 'result' in response:
            result = {"response": response['result']}
        else:
            # Try to find any string value in the response
            result = {"response": str(response)}
    else:
        result = {"response": str(response)}

    print(json.dumps(result, ensure_ascii=False, indent=2))

  except Exception as e:
      print(json.dumps({"error": f"An error occurred: {str(e)}"}))
      sys.exit(1)

if __name__ == "__main__":
    main()
