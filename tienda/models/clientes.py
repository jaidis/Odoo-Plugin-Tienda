from odoo import models, fields, api, _


class Clientes(models.Model):
    _name = 'tienda.clientes'
    # codigo = fields.Integer('Codigo', required=True)
    # marca = fields.Char('Marca', required=True)
    dni = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    direccion = fields.Char('Dirección', required=False)
    poblacion = fields.Char('Población', required=False)
    provincia = fields.Char('Provincia', required=False)
    codPostal = fields.Integer('Cod Postal', required=False)
    telefono = fields.Integer('Telefono', required=True)
    email = fields.Char('Email', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.dni + ' - ' + record.nombre + ' ' + record.apellidos
            res.append((record.id, name))
        return res
