class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        # letter_logs.sort(key=lambda log: (' '.join(log.split()[1:]), log.split()[0]))
        letter_logs.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        return letter_logs + digit_logs
