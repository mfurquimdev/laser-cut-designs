#!/bin/env python3


def main():
    custo_xerox = 7.5
    custo_transporte = 5.5 + 5.5
    tempo_transporte = 1 + 1
    tempo_design = 7
    custo_acrilico = 290 / 3
    custo_recorte = 480
    quantidade_pecas = 20
    lucro_em = 6

    custo_hora = 36

    material_corte = custo_acrilico + custo_recorte

    custo_tempo = (tempo_design + tempo_transporte) * custo_hora
    sub_total = custo_xerox + custo_transporte + material_corte
    total = sub_total + custo_tempo
    total_por_peca = total / quantidade_pecas

    print(f"custo_tempo = {custo_tempo}")
    print(f"material + corte = {material_corte}: {material_corte/quantidade_pecas}")
    print(f"sub_total = {sub_total}: {sub_total/quantidade_pecas}")
    print(f"total = {total}: {total/quantidade_pecas}")

    print(f"\nlucro em {lucro_em}: {sub_total/lucro_em}")
    vende_a = 75
    lucro_em = sub_total / vende_a
    print(f"vende a {vende_a} lucro em {lucro_em}")


if __name__ == "__main__":
    main()
