from project.app.models.Performance import Performance


class PerformanceRepository:
    @staticmethod
    def getting_performance_by_id(args, session):
        result = (
            session.query(Performance)
            .filter(Performance.performance_id == args.get("performance_id"))
            .first()
        )
        return result

    @staticmethod
    def add_performance(args, session):
        try:
            performance = Performance(**args)
            session.add(performance)
            session.commit()
            return performance
        except Exception as e:
            raise e

    @staticmethod
    def updating_performance(args, session, performance):
        if args.get("review_date"):
            performance.review_date = args["review_date"]
        if args.get("score"):
            performance.score = args["score"]
        if args.get("feedback"):
            performance.feedback = args["feedback"]
        if args.get("employee_id"):
            performance.employee_id = args["employee_id"]
        session.commit()
        return performance
