def init(self, actual_floor, elevator_floor, desired_floor, stranger_floor, stranger_desired_floor):
        
    self.stranger_desired_floor = stranger_desired_floor
        
    self.stranger_floor = stranger_floor
        
    waiting_time = abs(actual_floor - desired_floor) + abs(actual_floor - elevator_floor)
        
    stranger_waiting_time = abs(stranger_floor - stranger_desired_floor) + abs(stranger_floor - elevator_floor)
        
    distance_stranger = abs(stranger_floor - elevator_floor)
        
    distance_me = abs(actual_floor - elevator_floor)
        
        
    if distance_me > distance_stranger:
        waiting_time = abs(actual_floor - desired_floor) + abs(actual_floor - elevator_floor)
        stranger_waiting_time = waiting_time + (abs(stranger_floor - stranger_desired_floor) +
                                                    abs(stranger_floor - desired_floor))
    elif distance_me < distance_stranger:
        waiting_time = abs(actual_floor - desired_floor) + abs(actual_floor - elevator_floor)
        stranger_waiting_time = stranger_waiting_time + (abs(actual_floor - desired_floor) +
                                                             abs(actual_floor - stranger_desired_floor))

        print(f'{actual_floor} é seu andar atual, {stranger_floor}  é o andar do estranho, {stranger_desired_floor} é o andar desejado do estranho, {elevator_floor} é o andar atual do elevador, {desired_floor} é o andar desejado, {waiting_time} + é o tempo estimado, em segundos, até seu destino, {stranger_waiting_time} + é o tempo estimado até o destino do estranho')

gabao = Waiting_list(10, 0, 0, 9, 0)
digol = Waiting_list(10, 0, 0, 15, 0)
