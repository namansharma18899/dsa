import multiprocessing
import pycurl
from io import BytesIO

def post_res():
    # Use the httpbin.org endpoint for testing POST requests
    url = 'http://httpbin.org/post'

    # Create a BytesIO object to hold the response
    response = BytesIO()

    # Initialize a pycurl object
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.POST, 1)

    # Example of POST data, replace with your actual data if needed
    post_data = {'key1': 'value1', 'key2': 'value2'}
    postfields = '&'.join([f"{k}={v}" for k, v in post_data.items()])

    c.setopt(c.POSTFIELDS, postfields)
    c.setopt(c.WRITEDATA, response)

    try:
        # Perform the request
        c.perform()
        
        # Check the status code
        status_code = c.getinfo(pycurl.RESPONSE_CODE)
        if status_code == 200:
            print("POST request successful")
        else:
            print(f"POST request failed with status code {status_code}")
        
    except pycurl.error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Cleanup
        c.close()

    # Get the response content
    response_value = response.getvalue().decode('utf-8')
    print(response_value)

def run_parallel_processes(n):
    processes = []
    for _ in range(n):
        p = multiprocessing.Process(target=post_res)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

if __name__ == '__main__':
    run_parallel_processes(128)

