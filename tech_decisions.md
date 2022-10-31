# Decisions

- `React`: `React` is the natural choice for us as everyone in the team are familiar with it. The interpolation between JS and JSX makes displaying objects/data alot easier. Additionally, having components in a fragment-like mechanism can make things more organized, modular and reusable. React's support for other component libraries like, `Chakra UI`, also accelerate frontend implementation.
- `Chakra UI`: Component library that can fasten frontend development with shorthand styleprops, themable and Dark mode support out of the box. It also understands responsive design without having us to create different CSS element for each screen size.
- `Heroku`: `Heroku` works straight out of the box. Its minimal config system is familiar to everyone in the founding team, as well as allowing us to deploy the app much quicker. `Heroku`'s add-ons are also a nice to have to monitor/add new services to the webapp.
- `PostgreSQL`: One of our biggest technical pillars is to "let the pros manage it", thus we settled on using `Heroku PostgreSQL` to manage our SQL cluster. We can take advantage of the free tier and the requests will be fast since it is integrated into Heroku. `PostgreSQL` also support Full text search which can come into handy with manually searching through the tables.
- `Flask`: We prefer `Flask` as it allows for higher degree for freedom of configuration. With that being said, `Flask` can be ready to launch with fewer configuration than that of `Django`. For a prototype of this scale, this will allow us to push our changes faster.
- `RDS`: We considered Heroku Postgres but while `RDS` and `Heroku`'s offerings are similar in functionality, we get more juice on AWS side of things. For example our storage space is higher and db snapshots are enabled by default with higher number of retained snapshots.
- `Postman`: Having a dedicated "CURL" application with a GUI to configure the HTTP request is a good tool in our arcenal which will help tremendously in debugging.
- `GitHub`: The platform that we are most familiar with, as well with the most features baked into the repository. Also this was a mandatory selection for our internal software fetch data from `GitHub` to allow for grading.
- `AWS Cloudwatch`: Built in with all AWS services, allow log keeping for any of our AWS choices: RDS.
- `Prettier`: Linter for HTML, JS, JSX, CSS.
- `Black`: Linter for Python.
- `GitHub Actions`: Built-in to `GitHub`, meaning that the workflow progress/configuration can be viewed within the repository.
- `Sentry`: Provided for free from organization. Provide breadcrumbs log tracings even on the frontend level, as well as API response code logging and tracing.
- `PyTorch`: We will be using `PyTorch` as it is the machine learning library that we are most familiar with and offers customization with the model creation. Additionally, compared to `Tensorflow`, `PyTorch` is easier to learn, thus any team member not too familiar with machine learning code can easily pick it up.
