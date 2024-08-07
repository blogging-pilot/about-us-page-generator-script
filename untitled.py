import os

def get_company_info():
    company_name = input("Enter the company name: ")
    mission_statement = input("Enter the mission statement: ")
    team_members = input("Enter the team members (comma separated): ")
    return company_name, mission_statement, team_members.split(',')

def generate_html(company_name, mission_statement, team_members):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us - {company_name}</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <header>
            <h1>About Us</h1>
        </header>
        <section>
            <h2>Our Mission</h2>
            <p>{mission_statement}</p>
        </section>
        <section>
            <h2>Meet the Team</h2>
            <ul>
    """
    for member in team_members:
        html_content += f"<li>{member.strip()}</li>\n"
    
    html_content += """
            </ul>
        </section>
    </body>
    </html>
    """
    return html_content

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    company_name, mission_statement, team_members = get_company_info()
    html_content = generate_html(company_name, mission_statement, team_members)
    write_to_file('about_us.html', html_content)
    print("HTML file 'about_us.html' generated successfully.")
    