class BaseCaseData:
    def __init__(self, case_number, description, if_execute, precondition, depend_key, url, method, data, cookie,
                 header, expect_method, expect_result, result, result_data):
        self.case_number = case_number
        self.description = description
        self.if_execute = if_execute
        self.precondition = precondition
        self.depend_key = depend_key
        self.url = url
        self.method = method
        self.data = data
        self.cookie = cookie
        self.header = header
        self.expect_method = expect_method
        self.expect_result = expect_result
        self.result = result
        self.result_data = result_data

    def __repr__(self):
        return 'case_number=' + str(self.case_number) + ',description=' + str(self.description) + ',if_execute=' + str(
            self.if_execute) + ',precondition=' + str(self.precondition) + ',depend_key=' + str(
            self.depend_key) + ',url=' + str(self.url) + ',method=' + str(self.method) + ',data=' + str(
            self.data) + ',cookie=' + str(self.cookie) + ',header=' + str(self.header) + ',expect_method=' + str(
            self.expect_method) + ',expect_result=' + str(self.expect_result) + ',result=' + str(
            self.result) + ',result_data=' + str(self.result_data)
