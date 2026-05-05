class HMSBaseExpection(Exception):
    def __init__(self, message="An error occured in the HMS"):
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionError(HMSBaseExpection):
    def __init__(self, message="Failed to connnect to the database"):
        super().__init__(message)


class DuplicateRecordError(HMSBaseExpection):
    def __init__(self, entity, field, value ):
        message = f"{entity} with {field} = {value} already exist"
