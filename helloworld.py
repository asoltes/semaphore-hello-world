import argparse

def hello_world_devops(company_name):
    print(f"Hello, world! Greetings to all the DevOps professionals at {company_name}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send greetings to DevOps professionals at a company.')
    parser.add_argument('--company', type=str, required=True, help='The name of the company')
    
    args = parser.parse_args()
    
    hello_world_devops(args.company)
