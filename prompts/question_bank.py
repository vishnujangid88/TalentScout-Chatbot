"""
Question bank for technical questions by technology.
"""
from typing import List, Dict
import random


# Technology-specific question bank
TECH_QUESTIONS: Dict[str, List[str]] = {
    "Python": [
        "Explain the difference between a list and a tuple in Python. When would you use each?",
        "What is a decorator in Python? Can you give an example of how you would use one?",
        "How does Python handle memory management? What is the difference between shallow and deep copy?",
        "Explain the Global Interpreter Lock (GIL) in Python. How does it affect multi-threading?",
        "What are Python generators? How do they differ from regular functions and when would you use them?",
        "Explain the difference between __str__ and __repr__ methods in Python.",
        "How do you handle exceptions in Python? What's the difference between try-except and try-finally?",
        "What are Python's magic methods? Give examples of some commonly used ones.",
        "Explain list comprehensions vs generator expressions. When would you prefer one over the other?",
        "How does Python's import system work? What's the difference between import and from import?"
    ],
    "Django": [
        "Explain the Django MVT (Model-View-Template) architecture. How does it differ from MVC?",
        "What are Django migrations? How do you create and apply them?",
        "Explain Django's ORM. How would you optimize a slow query?",
        "What is Django middleware? Can you give an example of custom middleware?",
        "How does Django handle user authentication? What's the difference between authentication and authorization?",
        "Explain Django's class-based views vs function-based views. When would you use each?",
        "What are Django signals? Give an example of when you would use them.",
        "How do you handle static files and media files in Django?",
        "Explain Django's caching framework. What caching backends have you used?",
        "What is Django REST Framework? How would you create a RESTful API endpoint?"
    ],
    "Flask": [
        "Explain Flask's application context and request context. Why are they important?",
        "How do you handle database connections in Flask? What's the difference between Flask-SQLAlchemy and raw SQLAlchemy?",
        "What are Flask blueprints? How do they help organize large applications?",
        "How do you handle authentication in Flask? Have you used Flask-Login or JWT?",
        "Explain Flask's template inheritance. How does it work with Jinja2?",
        "What is Flask's g object? When would you use it?",
        "How do you handle errors and exceptions in Flask?",
        "Explain Flask's request lifecycle. What happens from when a request comes in to when a response is sent?",
        "How would you structure a large Flask application?",
        "What are Flask extensions you've used? Which ones are essential?"
    ],
    "React": [
        "Explain the difference between functional components and class components in React. When would you use each?",
        "What are React hooks? Explain useState and useEffect with examples.",
        "How does React's virtual DOM work? Why is it faster than direct DOM manipulation?",
        "Explain React's component lifecycle. How do hooks map to lifecycle methods?",
        "What is state management in React? When would you use Redux vs Context API?",
        "Explain React's reconciliation algorithm. How does React decide what to re-render?",
        "What are controlled vs uncontrolled components? Give examples of each.",
        "How do you handle side effects in React? What's the difference between useEffect and useLayoutEffect?",
        "Explain React's key prop. Why is it important and what happens if you don't use it?",
        "What is code splitting in React? How would you implement it?"
    ],
    "JavaScript": [
        "Explain the difference between var, let, and const in JavaScript. What are their scoping rules?",
        "What is the event loop in JavaScript? How does it handle asynchronous operations?",
        "Explain closures in JavaScript. Can you give a practical example?",
        "What is the difference between == and === in JavaScript? Why should you prefer ===?",
        "Explain promises and async/await in JavaScript. How do they differ from callbacks?",
        "What is hoisting in JavaScript? How does it work with different declarations?",
        "Explain the 'this' keyword in JavaScript. How does its value get determined?",
        "What are arrow functions? How do they differ from regular functions?",
        "Explain JavaScript's prototypal inheritance. How does it differ from classical inheritance?",
        "What are JavaScript modules? Explain the difference between CommonJS and ES6 modules."
    ],
    "Node.js": [
        "Explain Node.js's event-driven, non-blocking I/O model. How does it handle concurrency?",
        "What is the difference between require() and import in Node.js?",
        "Explain Node.js streams. When would you use readable, writable, or transform streams?",
        "How do you handle errors in Node.js? What's the difference between error-first callbacks and promises?",
        "What is the Node.js event loop? Explain the different phases.",
        "How do you manage dependencies in Node.js? Explain package.json and node_modules.",
        "What are middleware in Express.js? How do they work?",
        "Explain Node.js clustering. How would you scale a Node.js application?",
        "How do you handle file operations in Node.js? What's the difference between sync and async methods?",
        "What is npm? Explain the difference between dependencies and devDependencies."
    ],
    "MongoDB": [
        "Explain the difference between SQL and NoSQL databases. When would you choose MongoDB?",
        "What are MongoDB indexes? How do you create and use them effectively?",
        "Explain MongoDB's aggregation pipeline. Give an example of a complex aggregation.",
        "What is sharding in MongoDB? When and why would you use it?",
        "How do you handle relationships in MongoDB? Compare embedded vs referenced documents.",
        "Explain MongoDB transactions. When were they introduced and what are their limitations?",
        "What is the difference between find() and findOne() in MongoDB?",
        "How do you optimize MongoDB queries? What tools do you use for query analysis?",
        "Explain MongoDB's replica sets. How do they provide high availability?",
        "What are MongoDB schemas? How do you enforce data validation?"
    ],
    "PostgreSQL": [
        "Explain PostgreSQL's ACID properties. How does it ensure data integrity?",
        "What are PostgreSQL indexes? Explain B-tree, Hash, and GIN indexes.",
        "How do you optimize slow queries in PostgreSQL? What tools do you use?",
        "Explain PostgreSQL transactions and isolation levels. When would you use each level?",
        "What are PostgreSQL views? How do they differ from materialized views?",
        "Explain PostgreSQL's JSON and JSONB data types. When would you use each?",
        "How do you handle database migrations in PostgreSQL?",
        "What is PostgreSQL's EXPLAIN command? How do you use it to analyze queries?",
        "Explain PostgreSQL's foreign keys and constraints. How do they maintain referential integrity?",
        "What are PostgreSQL stored procedures? How do they differ from functions?"
    ],
    "AWS": [
        "Explain the difference between EC2, Lambda, and ECS. When would you use each?",
        "What is AWS S3? Explain different storage classes and when to use them.",
        "How do you secure AWS resources? Explain IAM roles and policies.",
        "What is AWS VPC? Explain subnets, route tables, and security groups.",
        "Explain AWS auto-scaling. How do you configure it for high availability?",
        "What are AWS CloudFormation and Terraform? How do they differ?",
        "How do you monitor AWS resources? Explain CloudWatch and its key features.",
        "What is AWS RDS? How does it differ from running a database on EC2?",
        "Explain AWS load balancing. What's the difference between ALB, NLB, and CLB?",
        "How do you handle secrets management in AWS? Explain AWS Secrets Manager."
    ],
    "Docker": [
        "Explain the difference between Docker images and containers. How do they relate?",
        "What is a Dockerfile? Explain key instructions like FROM, RUN, COPY, and CMD.",
        "How do you optimize Docker images? What are multi-stage builds?",
        "Explain Docker volumes. When would you use named volumes vs bind mounts?",
        "What is Docker Compose? How do you use it to orchestrate multiple containers?",
        "How do you handle environment variables in Docker?",
        "Explain Docker networking. How do containers communicate with each other?",
        "What is the difference between CMD and ENTRYPOINT in a Dockerfile?",
        "How do you debug a running Docker container?",
        "Explain Docker's layer caching. How does it affect build times?"
    ],
    "Kubernetes": [
        "Explain Kubernetes pods, services, and deployments. How do they work together?",
        "What is a Kubernetes namespace? When would you use multiple namespaces?",
        "How do you handle configuration in Kubernetes? Explain ConfigMaps and Secrets.",
        "Explain Kubernetes scaling. How do you configure horizontal pod autoscaling?",
        "What are Kubernetes ingress controllers? How do they differ from services?",
        "How do you manage stateful applications in Kubernetes? Explain StatefulSets.",
        "What is a Kubernetes service mesh? Have you used Istio or Linkerd?",
        "Explain Kubernetes resource limits and requests. Why are they important?",
        "How do you handle rolling updates in Kubernetes?",
        "What is Helm? How does it help manage Kubernetes applications?"
    ],
    "TensorFlow": [
        "Explain the difference between TensorFlow 1.x and 2.x. What are the key improvements?",
        "What is a TensorFlow session? How does it work in TF 2.x?",
        "Explain TensorFlow's eager execution vs graph execution.",
        "How do you build and train a neural network in TensorFlow?",
        "What are TensorFlow placeholders? How are they used in TF 2.x?",
        "Explain TensorFlow's data pipeline. How do you use tf.data?",
        "How do you save and load TensorFlow models?",
        "What is TensorFlow Serving? How do you deploy models with it?",
        "Explain TensorFlow's automatic differentiation. How does it work?",
        "How do you handle overfitting in TensorFlow models?"
    ],
    "PyTorch": [
        "Explain the difference between TensorFlow and PyTorch. When would you choose PyTorch?",
        "What are PyTorch tensors? How do they differ from NumPy arrays?",
        "Explain PyTorch's autograd system. How does automatic differentiation work?",
        "How do you build a neural network in PyTorch? Explain nn.Module.",
        "What is the difference between torch.no_grad() and torch.enable_grad()?",
        "Explain PyTorch's DataLoader. How do you create custom datasets?",
        "How do you save and load PyTorch models?",
        "What is the difference between model.train() and model.eval() in PyTorch?",
        "Explain PyTorch's device management. How do you use GPU?",
        "How do you implement custom loss functions in PyTorch?"
    ],
    "Angular": [
        "Explain Angular's component architecture. How do components communicate?",
        "What are Angular services? How do you inject dependencies?",
        "Explain Angular's change detection mechanism. How does it work?",
        "What are Angular modules? How do they differ from JavaScript modules?",
        "Explain Angular routing. How do you implement lazy loading?",
        "What are Angular directives? Explain structural vs attribute directives.",
        "How do you handle forms in Angular? Compare template-driven vs reactive forms.",
        "Explain Angular's dependency injection system.",
        "What are Angular pipes? How do you create custom pipes?",
        "How do you optimize Angular applications? Explain OnPush change detection strategy."
    ],
    "Vue.js": [
        "Explain Vue's reactivity system. How does it track changes?",
        "What are Vue components? How do you pass data between parent and child components?",
        "Explain Vue's lifecycle hooks. When would you use each?",
        "What is Vuex? How does it help with state management?",
        "Explain Vue Router. How do you implement navigation guards?",
        "What are Vue directives? Explain v-if, v-for, and v-model.",
        "How do you handle forms in Vue?",
        "Explain Vue's computed properties vs methods. When would you use each?",
        "What are Vue mixins? How do they differ from composition API?",
        "How do you optimize Vue applications? Explain lazy loading and code splitting."
    ],
    "Java": [
        "Explain the difference between abstract classes and interfaces in Java. When would you use each?",
        "What is the difference between == and equals() in Java?",
        "Explain Java's garbage collection. How does it work?",
        "What are Java generics? How do they provide type safety?",
        "Explain Java's exception handling. What's the difference between checked and unchecked exceptions?",
        "What is the difference between String, StringBuffer, and StringBuilder in Java?",
        "Explain Java's multithreading. How do you create and manage threads?",
        "What are Java annotations? Give examples of built-in and custom annotations.",
        "Explain Java's access modifiers. What's the difference between public, private, protected, and package-private?",
        "What is the Java Virtual Machine (JVM)? How does it execute Java code?"
    ],
    "Spring Boot": [
        "Explain Spring Boot's auto-configuration. How does it work?",
        "What are Spring Boot starters? How do they simplify dependency management?",
        "Explain Spring's dependency injection. How does it work with annotations?",
        "What is Spring Boot Actuator? What endpoints does it provide?",
        "Explain Spring Boot's profile system. How do you use different profiles?",
        "What are Spring Boot annotations? Explain @RestController, @Service, and @Repository.",
        "How do you handle database operations in Spring Boot? Explain JPA and Hibernate.",
        "Explain Spring Security. How do you implement authentication and authorization?",
        "What is Spring Boot's application.properties vs application.yml?",
        "How do you handle exceptions in Spring Boot? Explain @ControllerAdvice."
    ]
}


def get_questions_for_tech(tech_stack: List[str], num_questions: int) -> Dict[str, List[str]]:
    """
    Get questions for a given tech stack.
    
    Args:
        tech_stack: List of technologies
        num_questions: Number of questions to generate per technology
    
    Returns:
        Dictionary mapping each technology to a list of questions
    """
    questions_by_tech = {}
    
    for tech in tech_stack:
        tech_normalized = tech.strip()
        
        # Try exact match first
        if tech_normalized in TECH_QUESTIONS:
            available_questions = TECH_QUESTIONS[tech_normalized]
            selected = random.sample(
                available_questions,
                min(num_questions, len(available_questions))
            )
            questions_by_tech[tech_normalized] = selected
        else:
            # Try case-insensitive match
            matched = False
            for key in TECH_QUESTIONS.keys():
                if key.lower() == tech_normalized.lower():
                    available_questions = TECH_QUESTIONS[key]
                    selected = random.sample(
                        available_questions,
                        min(num_questions, len(available_questions))
                    )
                    questions_by_tech[tech_normalized] = selected
                    matched = True
                    break
            
            # If no match found, use generic questions
            if not matched:
                questions_by_tech[tech_normalized] = [
                    f"Can you explain your experience with {tech_normalized}?",
                    f"What are the key features of {tech_normalized} that you find most useful?",
                    f"Describe a project where you used {tech_normalized}. What challenges did you face?",
                    f"How would you approach learning a new feature in {tech_normalized}?",
                    f"What best practices do you follow when working with {tech_normalized}?"
                ][:num_questions]
    
    return questions_by_tech


def get_all_available_techs() -> List[str]:
    """Get a list of all technologies in the question bank."""
    return list(TECH_QUESTIONS.keys())


