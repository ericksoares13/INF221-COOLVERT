from app import bd

class Match(bd.Model):
    __tablename__ = 'match'
    
    id = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    id_musico = bd.Column(bd.Integer, bd.ForeignKey('musico.id'), nullable=False)
    id_demanda = bd.Column(bd.Integer, bd.ForeignKey('demanda.id'), nullable=False)

    def __repr__(self):
        return f'<({self.id}) {self.id_musico} {self.id_demanda}>'