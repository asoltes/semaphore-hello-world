import sys

def hello_world_devops(company_name):
    print(f"Hello, world! Greetings to all the DevOps professionals at {company_name}!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hello_world_devops.py <company_name>")
    else:
        company_name = sys.argv[1]
        hello_world_devops(company_name)
