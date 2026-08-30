---
Language: Go
tags:
 - wireguard
 - networking
 - cli-tool
 - nat-traversal
 - vpn
aliases:
 - Tailcat
 - tailcat CLI
 - derpcat
url: https://github.com/tailscale/tailcat
---
Tailcat은 Tailscale의 데이터 플레인(magicsock, WireGuard, DERP)을 재활용하여, Tailscale 계정이나 컨트롤 플레인 없이 netcat처럼 동작하는 CLI 도구 및 Go 라이브러리입니다. 서버 측에서 생성한 연결 토큰을 클라이언트가 전달받아 out-of-band로 연결을 맺고, 모든 트래픽은 WireGuard로 종단 간 암호화되며 NAT 홀펀칭을 통해 가능한 경우 직접 P2P 연결로 업그레이드됩니다. 루트 권한이나 시스템 네트워크 설정 변경 없이 사용자 공간에서 동작하며, 포트 포워딩, 인증 없는 SSH, SOCKS5 프록시, exit node 등 다양한 터널링 기능을 제공합니다.