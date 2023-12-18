# AI Prompt Engineering for Programmers

[Course Link](https://academy.zenva.com/course/ai-prompt-engineering-for-developers/)

## Lessons

### Code Generation

- Prompt the AI to generate code in almost any language you choose.
- You can use plain language or pseudocode.
- You can use it to add comments to your existing code.
- You can use it to convert a code snippet from one language to another.
- You can use it to generate placeholder data.
  - Can also be used to pull data from the internet.

#### Example Prompts
```text
Write a python script to do the following:

import an image, extract a color palette, dump 5 colors to the console
```

```text
Initialize a Python dictionary using the following values:

1, 2, 3, ...
```

```text
Add comments to the following code that a beginner will understand:

...
```

```text
Convert the following code from Python to C#:

...
```

```text
Generate a 15 record CSV file with this placeholder data:

username, password, email, ...
```

```text
Generate a python dictionary for each country in Europe with the value representing the country's population.
```

### Code Optimization

- Can be used to shrink code size, remove redundancy, and reinforce best practices.
  - This will often include details on what can be optimized and why it can be. Helps you learn why the change makes sense.
- Can be used to extract parent classes - promotes better inheritance/polymorphism
- Can be used to reinforce code standards
- Can be used to help break code down (single responsibility principle)

#### Example Prompts
```text
Optimize this Python code:

...
```

```text
Format this code to meet the C# coding standards:

...
```

```text
What are the main things to keep in mind when coding in C# with regards to coding standards?
```

```text
The following script is too large. Can you break it into smaller classes?

...
```

### Development Tools

- Can be used to write a git commit message for your code changes.
- Can be used to write a gitignore file for a project
- Can be used to write unit testing
- Can be used to generate documentation
- Can be used to learn more about frameworks and libraries
- Can be used to help structure your projects

#### Example Prompts
```text
Write a Git commit message for the following code:

...
```

```text
Write a Git commit message for the changes made to the following code.

Here is the current version:

...


Here is the version with my changes:

...
```

```text
Create a gitignore file for a Python project using TensorFlow, Pandas, and OpenCV
```

```text
Generate a unit text for the following Python code:

...
```

```text
Generate 5 tests for the following code:

...
```

```text
I want to test the following function. Give me 20 example parameters that will test all possible scenarios for this code:

...
```

```text
Write a one page document outlining the following code and what it does. Clearly define all inputs and outputs.
```

```text
I want to process image files. What are the top 5 python libraries that help with this task?
```

```text
Show me an example using the library ... to process this data.
```

```text
What is the standard structure for a python project?
```

```text
What file structure should I use for a new angular project?
```

### Getting the Desired Response

#### Assuming an Identity

- Tell the AI to act as a "professional" or expert in a certain field can improve your results.
  - Example: You are a... senior programmer, teacher, etc.
  - Example: You are an expert in the C# language and you are an expert in explaining complex topics in simple terms...

#### Your skill level

- Inform the AI on your skill level to help it know how much detail/how to explain something to you
  - Example: I am... a total beginner, fairly proficient in this language, etc...

#### Step by Step

- Inform the AI that you'd like it to present its response in a step by step format.
  - Example: Show me an example of inheritance in C#, step-by-step.

#### Style

- The style and format of the AI's response can be influenced by you
  - Example: ... Return the result in a table format.
  - Example: ... Provide 5 example courses on this topic. Bold the course name and provide a one sentence description of each.
  - Example: In one paragraph, ...
  - Example: In 30 words, ...
  - Example: In bullet points, ...
  - Example: Explain object-oriented programming as a song.
  - Example: Teach me about ... in the style of a first-person journal entry.

#### Reference

- You can ask the AI to provide a references to its response.
  - Example: What is the holy grail? Provide references for your response.
  - Example: What is networking? Provide references to books that will help me learn more about it.

### General Tips

#### Context

- The AI only knows as much as you provide.
- You can fine tune the response by giving it as much info as possible.

#### Give Examples

- If you want it to generate something, providing examples to the AI will help format its output.

#### Summarize

- The AI has a memory of your entire conversation. This allows it to remember things you told it in the past.
- You can use this to summarize what you've been working on.
- Example: Based on our conversation, what are 5 key takeaways?

#### Elaborate

- Like in a real conversation, you can ask the AI to elaborate on certain things to dive deeper on a topic.
