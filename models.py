import time

from app import db, session, Base

# id записи, id приложения, текущее дата и время int (unix timestamp), информационное сообщение от приложения.


class appInfo(Base):
    __tablename__ = 'appInfo'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False, default=lambda: int(time.time()*1000))
    message = db.Column(db.String(512), nullable=True)


# запись через консоль var = appInfo(app_id = 999, message = "OK")
# ЗАПРОС К БД для SQLAlchemy
# q = session.query(appInfo.app_id, func.max(appInfo.date).group_by(appInfo.app_id).having(func.max(appInfo.ts) < (time.time()-N*60)*1000)



