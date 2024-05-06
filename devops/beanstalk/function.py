def check_application_status(beanstalk, ApplicationNames) -> bool:
    try:
        applications = beanstalk.describe_applications(
            ApplicationNames=ApplicationNames
        )

        return True if len(applications['Applications']) > 0 else False
    except:
        return False
