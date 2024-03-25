class Solution:
    def interpret(self, command: str) -> str:
        for char in command:
           command = command.replace('()','o')
           command = command.replace('(al)','al')
        return command
