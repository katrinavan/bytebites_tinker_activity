# 🍔 ByteBites Tinker Activity

## 📌 Project Overview

The goal of this project was to design and implement the backend structure for a fictional food-ordering app called **ByteBites**. Starting from a written feature request, the system was broken into four core classes: `Customer`, `FoodItem`, `Menu`, and `Transaction`. Each class was designed to represent one part of the app’s functionality, such as storing customer history, representing menu items, filtering menu options, and calculating order totals. The project also included UML drafting, scaffold creation, algorithmic methods, and test validation. Overall, this activity emphasized how planning and design decisions directly shape code structure.

---

## 🧠 Key Concept Learned

The main concept students needed to understand was how to translate a **feature request** into a set of classes, attributes, methods, and relationships. Instead of jumping straight into code, students had to identify what the system needed to model and decide how responsibilities should be divided across classes. This required understanding the difference between **data storage** and **behavior**. For example, a `FoodItem` stores item information, while a `Menu` handles filtering, and a `Transaction` calculates totals. The activity reinforced the idea that good object-oriented design starts with careful interpretation of requirements, not just writing code quickly.

---

## ⚠️ Common Struggles

One of the places students are most likely to struggle is deciding **which class should own a behavior**. It can be easy to mix up responsibilities, such as putting total calculation inside `Menu` instead of `Transaction`, or creating extra classes that were never requested. Another common challenge is knowing how much detail to include in early scaffolds versus later implementations. Students may also struggle with keeping their UML diagram aligned with the original spec, especially when AI tools suggest more advanced or unnecessary features. Finally, testing can feel confusing at first because students have to connect expected outputs back to the underlying class design.

---

## 🤖 Where AI Helped

AI was most helpful during the **brainstorming and planning stages**. It was useful for turning the written prompt into a first-pass UML diagram, identifying possible class responsibilities, and creating simple scaffolds for `models.py`. AI also helped speed up repetitive work like drafting boilerplate constructors, suggesting method names, and providing a starting point for test cases. In this project, AI was especially useful when refining code structure and checking whether the implementation still matched the original spec. Used well, AI served as a strong planning assistant and debugging partner.

---

## 🚩 Where AI Could Be Misleading

AI could also be misleading when it became too ambitious. In several cases, AI-generated code added extra classes, methods, and validations that were not actually required by the ByteBites prompt. For example, it might introduce things like separate `Price`, `Category`, or catalog-style classes even though the assignment only asked for four main classes. This can make the design look more advanced, but it actually pulls the project away from the spec. AI can also blur the line between a **simple scaffold** and a **fully built system**, which may cause students to overcomplicate their work. Because of that, students still need to compare every AI suggestion back to the original feature request.

---

## 🧩 How I Would Guide a Student

One way I would guide a student without giving away the answer is by asking them to point to **one specific sentence in the feature request** and explain which class should handle it. Then I would ask them why that responsibility belongs there and not somewhere else. This keeps the student grounded in the prompt and helps them reason through the design instead of copying an answer. If they are stuck, I would encourage them to map each requirement to either an attribute, a method, or a relationship. That approach gives support while still leaving the student responsible for making the final design decisions.

---

## 🛠 Project Files

| File | Purpose |
|------|---------|
| `bytebites_spec.md` | Original feature request and candidate classes |
| `draft_from_copilot.md` | Initial UML draft |
| `bytebites_design.md` | Final revised UML design |
| `models.py` | Python class scaffolds and implemented methods |
| `test_bytebites.py` | Pytest tests for totals and filtering |
| `README.md` | Project summary and reflection |

---

## ✅ Final Takeaway

This project showed that building software is creating a design implementation first before diving into straight coding. The ByteBites activity made that process visible step by step, from spec to UML to scaffolds to algorithms to tests. It also highlighted that AI can be a helpful collaborator, but only when students stay focused on the actual assignment requirements. The strongest designs came from using AI as support, not as a replacement for reasoning.

---