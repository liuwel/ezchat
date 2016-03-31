<?php
/**
 * Created by PhpStorm.
 * User: liuwel
 * Date: 16-3-30
 * Time: 下午10:30
 */
$serv = new swoole_websocket_server("0.0.0.0", 9502);

$serv->on('Open', function($server, $req) {
    echo "open: " . $req->fd . "\n";
    $server->push($req->fd,json_encode(['cmd'=>'init','fd'=>$req->fd]));
});

$serv->on('Message', function($server, $frame) {
    $data = json_decode($frame->data);
    if(is_null($data)){
        return;
    }
    switch($data->command){
        case 'checkToken':
            login($frame->fd,$data->options->token);
            break;
        case 'init':
            echo "init\n";
            break;
        default:
            pushAll($server, $frame);
            break;
    }
});

$serv->on('Close', function($server, $fd) {
    echo "connection close: ".$fd;
    logout($fd);
});

$serv->start();


function pushAll($server,$frame){
    foreach($server->connections as $fd){
        $server->push($fd,json_encode($frame->data));
    }
}

function login($fd,$token){

}

function logout($fd){

}


/**
 * 缓存
 * Class Cache
 */
class Cache{

    private $_cache = null;

    public function get($key){
        $cache = $this->getMemcached();
        return $cache->get($key);
    }

    public function set($key,$value,$expiration=0){
        $cache = $this->getMemcached();
        return $cache->set($key,$value,$expiration);
    }

    public function getMemcached(){
        if( !($this->_cache instanceof Memcached) ){
            $this->_cache = new Memcached();
            $this->_cache->addServer('127.0.0.1',11211);
        }
        return $this->_cache;
    }
}