import random
import sys

import pygame

LARGURA, ALTURA = 900, 560
FPS = 60

BRANCO = (245, 245, 245)
PRETO = (25, 25, 30)
CINZA = (70, 75, 85)
FUNDO = (35, 40, 52)
VERDE = (80, 200, 120)
VERMELHO = (220, 80, 80)
AMARELO = (240, 200, 80)
AZUL = (90, 150, 230)

PRODUTOS = [
    {"nome": "Pão", "preco": 5, "custo": 2, "cor": (210, 160, 90)},
    {"nome": "Leite", "preco": 8, "custo": 4, "cor": (200, 220, 240)},
    {"nome": "Café", "preco": 15, "custo": 8, "cor": (130, 90, 60)},
]
LOTE = 5
PACIENCIA = 12.0  # segundos
MAX_FILA = 5


class Botao:
    def __init__(self, rect, texto, cor):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.cor = cor

    def desenhar(self, tela, fonte, ativo=True):
        cor = self.cor if ativo else CINZA
        mouse_em_cima = self.rect.collidepoint(pygame.mouse.get_pos())
        if ativo and mouse_em_cima:
            cor = tuple(min(255, c + 25) for c in cor)
        pygame.draw.rect(tela, cor, self.rect, border_radius=8)
        img = fonte.render(self.texto, True, PRETO)
        tela.blit(img, img.get_rect(center=self.rect.center))

    def clicado(self, pos):
        return self.rect.collidepoint(pos)


class Cliente:
    def __init__(self):
        self.produto = random.randrange(len(PRODUTOS))
        self.paciencia = PACIENCIA
        self.cor = random.choice([(230, 120, 120), (120, 200, 230), (180, 140, 230), (140, 220, 140)])


class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Loja de Vendas")
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.SysFont("arial", 20)
        self.fonte_g = pygame.font.SysFont("arial", 30, bold=True)
        self.fonte_p = pygame.font.SysFont("arial", 16)
        self.botoes = []
        for i in range(len(PRODUTOS)):
            x = 40 + i * 285
            self.botoes.append((
                Botao((x, 440, 120, 40), "Vender", VERDE),
                Botao((x + 130, 440, 120, 40), f"Repor +{LOTE}", AZUL),
            ))
        self.reiniciar()

    def reiniciar(self):
        self.dinheiro = 50
        self.reputacao = 5
        self.vendidos = 0
        self.estoque = [5, 5, 5]
        self.fila = []
        self.tempo_prox = 2.0
        self.mensagem = ""
        self.msg_tempo = 0
        self.fim = False
        self.tempo_total = 0

    def aviso(self, texto):
        self.mensagem = texto
        self.msg_tempo = 2.0

    def vender(self, i):
        if not self.fila:
            self.aviso("Não há clientes na fila.")
            return
        cliente = self.fila[0]
        if self.estoque[i] <= 0:
            self.aviso(f"Sem estoque de {PRODUTOS[i]['nome']}!")
            return
        self.estoque[i] -= 1
        if cliente.produto == i:
            self.dinheiro += PRODUTOS[i]["preco"]
            self.vendidos += 1
            self.aviso(f"Vendeu {PRODUTOS[i]['nome']}! +R${PRODUTOS[i]['preco']}")
        else:
            self.reputacao -= 1
            self.aviso("Produto errado! -1 reputação")
        self.fila.pop(0)

    def repor(self, i):
        custo = PRODUTOS[i]["custo"] * LOTE
        if self.dinheiro >= custo:
            self.dinheiro -= custo
            self.estoque[i] += LOTE
            self.aviso(f"Repôs {LOTE} {PRODUTOS[i]['nome']} (-R${custo})")
        else:
            self.aviso("Dinheiro insuficiente!")

    def atualizar(self, dt):
        if self.fim:
            return
        self.tempo_total += dt
        self.msg_tempo = max(0, self.msg_tempo - dt)

        # chegada de clientes (fica mais rápido com o tempo)
        self.tempo_prox -= dt
        if self.tempo_prox <= 0 and len(self.fila) < MAX_FILA:
            self.fila.append(Cliente())
            self.tempo_prox = max(1.5, random.uniform(2.5, 5.0) - self.tempo_total / 60)

        # paciência
        for c in self.fila[:]:
            c.paciencia -= dt
            if c.paciencia <= 0:
                self.fila.remove(c)
                self.reputacao -= 1
                self.aviso("Um cliente foi embora! -1 reputação")

        if self.reputacao <= 0:
            self.fim = True

    def desenhar(self):
        self.tela.fill(FUNDO)
        pygame.draw.rect(self.tela, (50, 56, 70), (0, 0, LARGURA, 60))
        topo = f"Dinheiro: R$ {self.dinheiro}    Reputação: {'♥' * max(0, self.reputacao)}    Vendas: {self.vendidos}"
        self.tela.blit(self.fonte_g.render(topo, True, BRANCO), (20, 12))

        # fila de clientes
        for idx, c in enumerate(self.fila):
            x = 90 + idx * 160
            y = 220
            pygame.draw.circle(self.tela, c.cor, (x, y), 30)
            pygame.draw.circle(self.tela, PRETO, (x - 10, y - 6), 4)
            pygame.draw.circle(self.tela, PRETO, (x + 10, y - 6), 4)
            pygame.draw.arc(self.tela, PRETO, (x - 12, y - 2, 24, 20), 3.4, 6.0, 2)
            prod = PRODUTOS[c.produto]
            balao = pygame.Rect(x - 45, y - 100, 90, 34)
            pygame.draw.rect(self.tela, BRANCO, balao, border_radius=10)
            txt = self.fonte_p.render(prod["nome"], True, PRETO)
            self.tela.blit(txt, txt.get_rect(center=balao.center))
            # barra de paciência
            frac = c.paciencia / PACIENCIA
            cor = VERDE if frac > 0.5 else AMARELO if frac > 0.25 else VERMELHO
            pygame.draw.rect(self.tela, CINZA, (x - 35, y + 42, 70, 8), border_radius=4)
            pygame.draw.rect(self.tela, cor, (x - 35, y + 42, 70 * frac, 8), border_radius=4)
            if idx == 0:
                seta = self.fonte_p.render("▲ atendendo", True, AMARELO)
                self.tela.blit(seta, seta.get_rect(center=(x, y + 68)))

        # painel de produtos
        for i, prod in enumerate(PRODUTOS):
            x = 40 + i * 285
            painel = pygame.Rect(x - 10, 340, 270, 150)
            pygame.draw.rect(self.tela, (50, 56, 70), painel, border_radius=12)
            pygame.draw.rect(self.tela, prod["cor"], (x, 352, 24, 24), border_radius=6)
            self.tela.blit(self.fonte.render(prod["nome"], True, BRANCO), (x + 34, 352))
            info = f"Preço: R${prod['preco']}   Custo lote: R${prod['custo'] * LOTE}"
            self.tela.blit(self.fonte_p.render(info, True, BRANCO), (x, 388))
            cor_est = VERMELHO if self.estoque[i] == 0 else BRANCO
            self.tela.blit(self.fonte.render(f"Estoque: {self.estoque[i]}", True, cor_est), (x, 410))
            b_vender, b_repor = self.botoes[i]
            b_vender.desenhar(self.tela, self.fonte, self.estoque[i] > 0 and bool(self.fila))
            b_repor.desenhar(self.tela, self.fonte, self.dinheiro >= prod["custo"] * LOTE)

        if self.msg_tempo > 0:
            img = self.fonte.render(self.mensagem, True, AMARELO)
            self.tela.blit(img, img.get_rect(center=(LARGURA // 2, 90)))

        if self.fim:
            sombra = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            sombra.fill((0, 0, 0, 180))
            self.tela.blit(sombra, (0, 0))
            t1 = self.fonte_g.render("FIM DE JOGO", True, VERMELHO)
            t2 = self.fonte.render(f"Vendas: {self.vendidos}   Dinheiro: R$ {self.dinheiro}", True, BRANCO)
            t3 = self.fonte.render("Pressione R para recomeçar", True, AMARELO)
            self.tela.blit(t1, t1.get_rect(center=(LARGURA // 2, 220)))
            self.tela.blit(t2, t2.get_rect(center=(LARGURA // 2, 270)))
            self.tela.blit(t3, t3.get_rect(center=(LARGURA // 2, 320)))

        pygame.display.flip()

    def executar(self):
        while True:
            dt = self.relogio.tick(FPS) / 1000
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_r and self.fim:
                    self.reiniciar()
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and not self.fim:
                    for i, (b_vender, b_repor) in enumerate(self.botoes):
                        if b_vender.clicado(ev.pos):
                            self.vender(i)
                        elif b_repor.clicado(ev.pos):
                            self.repor(i)
            self.atualizar(dt)
            self.desenhar()


if __name__ == "__main__":
    Jogo().executar()