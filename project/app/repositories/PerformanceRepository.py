from project.app.models.Performance import Performance


class PerformanceRepository:
    @staticmethod
    def add_performance(args, session):
        try:
            performance = Performance(**args)
            session.add(performance)
            session.commit()
            return performance
        except Exception as e:
            raise e
