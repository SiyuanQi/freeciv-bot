'''
Created on 09.03.2018

@author: christian
'''
from utils.base_state import ListState

class UnitState(ListState):
    def __init__(self, unit_ctrl, rule_ctrl, city_ctrl):
        ListState.__init__(self)
        self.unit_ctrl = unit_ctrl
        self.rule_ctrl = rule_ctrl
        self.city_ctrl = city_ctrl
        
    def _update_state(self, pplayer):
        """
            Function returns the current state of all units of player pplayer
        """
        for unit_id in self.unit_ctrl.units.keys():
            punit = self.unit_ctrl.units[unit_id]
            if punit["owner"] == pplayer["playerno"]:
                self._state[unit_id] = self._get_unit_infos(punit)

    def _get_unit_infos(self, aunit):
        unit_state = {}

        ptype = self.rule_ctrl.unit_type(aunit)
        for type_desc in ["name", "helptext", "attack_strength", "defense_strength", "firepower"]:
            unit_state["type_"+type_desc] = ptype[type_desc]
        unit_state["can_transport"] = ptype['transport_capacity'] > 0
        unit_state["home_city"] = self.city_ctrl.get_unit_homecity_name(aunit)
        unit_state["moves_left"] = self.unit_ctrl.get_unit_moves_left(aunit)
        unit_state["health"] = aunit['hp']
        unit_state["veteran"] = aunit['veteran']
        return unit_state