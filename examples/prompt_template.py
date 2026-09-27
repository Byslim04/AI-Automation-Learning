def generate_prompt(task_description: str) -> str
    return f"Выполнить следующую задачу: {task_description}"
if __name__ == "__main__":
    prompt = generate_prompt("Напиши короткий приветственный текст")
    print(prompt)



------------


def generate_prompt(task_description: str) -> str:
    return f"Complete the following task: {task_description}"

if name == "main":
    prompt = generate_prompt("Write a short greeting text")
    print(prompt)
