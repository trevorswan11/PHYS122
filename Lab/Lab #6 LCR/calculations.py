from math import sqrt, pow
import time

# trial values - R includes the resistance of the inductor!
# L, DL, C, DC, R, DR

one_1 = [0.0866, 0.0001, 2.2 * pow(10, -8), pow(10, -9), 188.8, 0.1] # no added resistor, 0.022 capacitor
two_1 = [0.0866, 0.0001, 4.8 * pow(10, -7), pow(10, -8), 188.8, 0.1] # no added resistor, 0.47 capacitor
three_1 = [0.0866, 0.0001, 4.8 * pow(10, -7), pow(10, -8), 287.9, 0.1414213562] # added 100 ohm resistor, 0.47 capacitor
four_1 = [0.0866, 0.0001, 4.8 * pow(10, -7), pow(10, -8), 681.3, 3.5] # added 500 ohm resistor, 0.47 capacitor
five_1 = [0.0866, 0.0001, 4.8 * pow(10, -7), pow(10, -8), 1178.8, 10.0] # added 1000 ohm resistor, 0.47 capacitor
six_1 = [0.0866, 0.0001, 4.8 * pow(10, -7), pow(10, -8), 2158.8, 14.1] # added 2000 ohm resistor, 0.47 capacitor

trials_first_part = [one_1, two_1, three_1, four_1, five_1, six_1]

# omega prime

def w(L, DL, C, DC, R, DR):
    return sqrt(1 / (L * C) - pow(R / (2 * L), 2))

def d_w_l(L, DL, C, DC, R, DR):
    numerator = C * pow(R, 2) - 2 * L
    denominator = 2 * pow(L, 2) * sqrt(C * (4 * L - C * pow(R, 2)))
    return (numerator / denominator) * DL

def d_w_c(L, DL, C, DC, R, DR):
    numerator = 1
    denominator = pow(C, 3/2) * sqrt(4 * L - C * pow(R, 2))
    return (numerator / denominator) * DC

def d_w_r(L, DL, C, DC, R, DR):
    numerator = sqrt(C) * R
    denominator = 2 * L * sqrt(4 * L - C * pow(R, 2))
    return (numerator / denominator) * DR

def d_w(d_w_l_calc, d_w_c_calc, d_w_r_calc):
    return sqrt(pow(d_w_l_calc, 2) + pow(d_w_c_calc, 2) + pow(d_w_r_calc, 2))

# tau

def t(L, DL, C, DC, R, DR):
    return (2 * L) / R

def d_t_L(L, DL, C, DC, R, DR):
    return (2 / R) * DL

def d_t_R(L, DL, C, DC, R, DR):
    return ((2 * L) / pow(R, 2)) * DR

def d_t(d_t_L_calc, d_t_R_calc):
    return sqrt(pow(d_t_L_calc, 2) +pow(d_t_R_calc, 2))

# Xi

def xi(L, DL, C, DC, R, DR):
    return (R / 2) * sqrt(C / L)

def d_xi_l(L, DL, C, DC, R, DR):
    return ((R / 4) * sqrt(C / pow(L, 3))) * DL

def d_xi_c(L, DL, C, DC, R, DR):
    return (R / (4 * sqrt(C * L))) * DC

def d_xi_r(L, DL, C, DC, R, DR):
    return (0.5 * sqrt(C / L)) * DR

def d_xi(d_xi_l_calc, d_xi_c_calc, d_xi_r_calc):
    return sqrt(pow(d_xi_l_calc, 2) + pow(d_xi_c_calc, 2) + pow(d_xi_r_calc, 2))

# runtime

def trial_calculation_1(list_input, trial_number):
    if (len(list_input) != 6): return
    if (trial_number > 4):
        return [
            t(*list_input),
            xi(*list_input)
        ]
    
    return [
        w(*list_input),
        t(*list_input),
        xi(*list_input)
    ]

def trial_error_calculation_1(list_input, trial_number):
    if (len(list_input) != 6): return
    if (trial_number > 4):
        return [
            d_t(d_t_R(*list_input), d_t_L(*list_input)),
            d_xi(d_xi_l(*list_input), d_xi_c(*list_input), d_xi_r(*list_input))
        ]
    
    return [
        d_w(d_w_l(*list_input), d_w_c(*list_input), d_w_r(*list_input)),
        d_t(d_t_R(*list_input), d_t_L(*list_input)),
        d_xi(d_xi_l(*list_input), d_xi_c(*list_input), d_xi_r(*list_input))
    ]

# trial values - R includes the resistance of the function generator when noted by variable name!
# L, DL, C, DC, R, DR

one_2_no_function_generator_resistance = [0.0866, 0.0001, 4.5 * pow(10, -9), pow(10, -10), 1178.8, 10]
two_2_yes_function_generator_resistance = [0.0866, 0.0001, 4.5 * pow(10, -9), pow(10, -10), 1228.8, 10]

second_part_data = [one_2_no_function_generator_resistance, two_2_yes_function_generator_resistance]

# omega sub r

def w_r(L, DL, C, DC, R, DR):
    return sqrt(1 / (L * C))

def d_w_r_l(L, DL, C, DC, R, DR):
    return (0.5 * C * pow(1 / (L * C), 3/2)) * DL

def d_w_r_c(L, DL, C, DC, R, DR):
    return (0.5 * L * pow(1 / (L * C), 3/2)) * DC

def d_w_r_tot(d_w_r_l_calc, d_w_r_c_calc):
    return sqrt(pow(d_w_r_l_calc, 2) + pow(d_w_r_c_calc, 2))

# Q

def q(L, DL, C, DC, R, DR):
    return (1 / R) * sqrt(L / C)

def d_q_l(L, DL, C, DC, R, DR):
    return ((1 / (L * R)) * sqrt(L / C)) * DL

def d_q_c(L, DL, C, DC, R, DR):
    return ((1 / (C * R)) * sqrt(L / C)) * DC

def d_q_r(L, DL, C, DC, R, DR):
    return ((1 / (R * R)) * sqrt(L / C)) * DR

def d_q(d_q_l_calc, d_q_c_calc, d_q_r_calc):
    return sqrt(pow(d_q_l_calc, 2) + pow(d_q_c_calc, 2) + pow(d_q_r_calc, 2))

def dataset_calculation_2(list_input):
    if (len(list_input) != 6): return
    
    return [
        q(*list_input),
        w_r(*list_input)
    ]
    
def dataset_error_calculation_2(list_input):
    if (len(list_input) != 6): return
    
    return [
        d_q(d_q_l(*list_input), d_q_c(*list_input), d_q_r(*list_input)),
        d_w_r_tot(d_w_r_l(*list_input), d_w_r_c(*list_input))
    ]

if __name__ == "__main__":
    start = time.perf_counter()
    
    print("Damped Oscillator Calculations:")
    for i, trial in enumerate(trials_first_part, 1):
        print(f"Trial {str(i)}:")
        result1 = trial_calculation_1(trial, i)
        result2 = trial_error_calculation_1(trial, i)
        if (len(result1) == 2):
            print(f"tau = {result1[0]} +/- {result2[0]}")
            print(f"xi = {result1[1]} +/- {result2[1]}")
            continue
        trial_w, trial_t, trial_xi = result1
        trial_dw, trial_dt, trial_dxi = result2
        print(f"omega = {trial_w} +/- {trial_dw}")
        print(f"tau = {trial_t} +/- {trial_dt}")
        print(f"xi = {trial_xi} +/- {trial_dxi}")
        
    print("\nResonant Circuit Calculations:")
    for i, dataset in enumerate(second_part_data, 1):
        print(f"Dataset {str(i)}:")
        result1 = dataset_calculation_2(dataset)
        result2 = dataset_error_calculation_2(dataset)
        dataset_q, dataset_w_r = result1
        dataset_dq, dataset_dw_r = result2
        print(f"q = {dataset_q} +/- {dataset_dq}")
        print(f"w_r = {dataset_w_r} +/- {dataset_dw_r}")
        
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"\nCalculations took: {elapsed_ms:.4f} ms")
        
# output
"""
Damped Oscillator Calculations:
    Trial 1:
        omega = 22884.29650922336 +/- 521.4444087809482
        tau = 0.0009173728813559321 +/- 1.1654435761341052e-06
        xi = 0.04757999463162536 +/- 0.001082005922815503
    Trial 2:
        omega = 4782.124617108206 +/- 52.46760756984916
        tau = 0.0009173728813559321 +/- 1.1654435761341052e-06
        xi = 0.22224585350358758 +/- 0.0023216006329009288
    Trial 3:
        omega = 4614.534046444006 +/- 54.35551481431524
        tau = 0.0006015977770059049 +/- 7.549286618055374e-07
        xi = 0.33890138360001515 +/- 0.003539558337300766
    Trial 4:
        omega = 2929.8013814492842 +/- 89.74282990603875
        tau = 0.00025421987377073244 +/- 1.3385737871276907e-06
        xi = 0.8019920550423422 +/- 0.009326292051353605
    Trial 5:
        tau = 0.00014692908042076688 +/- 1.2579235983829609e-06
        xi = 1.387624004820069 +/- 0.018658514492621684
    Trial 6:
        tau = 8.022975727255882e-05 +/- 5.321397357121021e-07
        xi = 2.5412306596586065 +/- 0.031278778228866655

Resonant Circuit Calculations:
    Dataset 1 (without function generator resistance):
        q = 3.721453201303495 +/- 0.08862414872350376
        w_r = 50656.45535446374 +/- 563.6088830836692
    Dataset 2 (with function generator resistance):
        q = 3.5700268828910806 +/- 0.08458688494560974
        w_r = 50656.45535446374 +/- 563.6088830836692

Calculations took: 0.7414 ms
"""