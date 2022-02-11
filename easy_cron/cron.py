import subprocess

def get_cron_list():
    cron_in        = subprocess.Popen(['crontab', '-l'], stdout=subprocess.PIPE)
    cur_crontab, _ = cron_in.communicate()

    return cur_crontab.decode("utf-8").split("\n")

def get_job_list():
    cron_list = get_cron_list()
    return [item.replace(";","").split(" ") for item in cron_list if len(item) > 1 and str(item)[0] != '#']

def validate_schedule(schedule):

    if not {"minute", "hour", "day_monthly", "month", "day_weekly"}.issubset(schedule.keys()):
        raise Exception("Schedule is missing keys")
    
    try:
        if schedule['minute'] != "*" and int(schedule['minute']) > 59:
            raise Exception("Invalid schedule input")
        if schedule['hour'] != "*" and int(schedule['hour']) > 23:
            raise Exception("Invalid schedule input") 
        if schedule['day_monthly'] != "*" and int(schedule['day_monthly']) > 31:
            raise Exception("Invalid schedule input")
        if schedule['month'] != "*" and int(schedule['month']) > 12:
            raise Exception("Invalid schedule input")
        if schedule['day_weekly'] != "*" and int(schedule['day_weekly']) > 7:        
            raise Exception("Invalid schedule input")
    
    except:
        raise Exception("Invalid schedule input")
    
def validate_command(command_str):
    if not len(command_str.split(" ")) >= 2:
        raise Exception("command is missing input")

def add_job(schedule, command_str):

    validate_command(command_str)
    validate_schedule(schedule)

    parsed_command    = command_str.split(" ")
    parsed_espression = [
        schedule['minute'],
        schedule['hour'],
        schedule['day_monthly'],
        schedule['month'],
        schedule['day_weekly'],
    ]
    
    set_job(parsed_espression, parsed_command)

def remove_job(command_str):

    validate_command(command_str)
    command_str = command_str.split(" ")
    new_command = command_str[0]
    new_input   = command_str[1]

    new_cron_list = []
    for job in get_job_list():

        curr_command = job[5]
        curr_input   = job[6]

        if curr_command == new_command and curr_input == new_input:
            continue
        elif job != None:
            new_cron_list.append(job)
    
    new_cron_list = [" ".join(item) for item in new_cron_list]
    set_cron_list(new_cron_list)

def set_job(parsed_expression, parsed_command):

    EXISTS = False

    new_command = parsed_command[0]
    new_input   = parsed_command[1]

    new_cron_list = []
    for job in get_job_list():

        curr_command = job[5]
        curr_input   = job[6]

        if curr_command == new_command and curr_input == new_input:
            replaced_job = parsed_expression + parsed_command
            new_cron_list.append(replaced_job)
            EXISTS = True
        elif job != None:
            new_cron_list.append(job)
    
    if not EXISTS:
        replaced_job = parsed_expression + parsed_command
        new_cron_list.append(replaced_job)

    new_cron_list = [" ".join(item) for item in new_cron_list]
    set_cron_list(new_cron_list)

# cron_list = ["# This is a commnet", "* * * * * echo hello", "* * * * * echo goodbye"]
# print(cron_list)

def set_cron_list(cron_list):
    new_crontab = str.encode("\n".join(cron_list))
    cron_out = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE)
    cron_out.communicate(input=new_crontab)


